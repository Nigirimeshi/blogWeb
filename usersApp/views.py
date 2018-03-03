import datetime
import hashlib

from django.shortcuts import render, redirect
from blogProject import settings

from .forms import RegisterForm
from .models import Email_Confirmation_Code
from .tasks import send_register_mail

REDIRECT_FIELD_NAME = 'next'


def register(request,
             redirect_field_name=REDIRECT_FIELD_NAME):
    """
    用户注册视图

    :param redirect_field_name: 重定向上一个页面 get 参数名
    """
    # get 请求中，next 通过 url 传递 ?next={{ request.path }}
    # post 请求中，next 通过表单传递 <input class="hidden" name="next" value="{{ next }}">
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            code = make_email_confirm_code(new_user)
            send_register_mail.delay(email=new_user.email, code=code)
            return redirect('usersApp:register_done')
            # if redirect_to:
            #     return redirect('usersApp:register_done')
            # else:
            #     return redirect('/')
    else:
        form = RegisterForm()

    context = {'form': form,
               'next': redirect_to,
               }
    return render(request, 'usersApp/register.html', context)


def register_confirm(request,
                     confirm_days=settings.CONFIRM_DAYS):
    """
    用户注册确认

    :param confirm_days: 注册邮件有效期
    :return:
    """
    code = request.GET.get('code', None)
    try:
        confirm = Email_Confirmation_Code.objects.get(code=code)
    except:
        message = '错误的注册验证信息！'
        return render(request, 'usersApp/register_confirm.html', {'message': message})

    created_time = confirm.created_time
    now = datetime.datetime.now()

    if now > created_time + datetime.timedelta(confirm_days):
        confirm.user.delete()
        message = '邮件过期了，已经失效了！(>_<) 重新注册一下吧'
    else:
        confirm.user.is_active = True
        confirm.user.save()
        confirm.delete()
        message = '注册成功啦，快去登陆吧！_(:з)∠)_'
    return render(request, 'usersApp/register_confirm.html', {'message': message})


def register_done(request):
    return render(request, 'usersApp/register_done.html')


def hash_sha256(key, salt='Huaji'):
    """
    加密

    :param key: 需要加密的关键字段
    :param salt: 给关键字段加点"盐"
    :return: 一个 sha256 加密的哈希值
    """
    sha256 = hashlib.sha256()
    key += salt
    sha256.update(key.encode())  # 需要 bit 类型
    return sha256.hexdigest()


def make_email_confirm_code(user):
    """
    制作注册用户的邮箱确认码
    在邮箱确认码添加关联用户表的数据

    :param user: 注册用户的实例对象
    :return: 关联到用户的确认码
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_sha256(user.username, now)
    Email_Confirmation_Code.objects.create(code=code, user=user)
    return code
