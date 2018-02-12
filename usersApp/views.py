from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from .forms import RegisterForm
from .models import User, Email_Confirmation_Code
from blogProject import settings

import hashlib
import datetime

REDIRECT_FIELD_NAME = 'next'


def register(request,
             redirect_field_name=REDIRECT_FIELD_NAME):
    # get 请求中，next 通过 url 传递 ?next={{ request.path }}
    # post 请求中，next 通过表单传递 <input class="hidden" name="next" value="{{ next }}">
    redirect_to = request.POST.get(redirect_field_name, request.GET.get(redirect_field_name, ''))

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            code = make_email_confirm_code(new_user)
            send_register_mail(email=new_user.email, code=code)
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
    code = request.GET.get('code', None)
    message = ''
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
    * 加密
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
    * 制作注册用户的邮箱确认码
    * 在邮箱确认码添加关联用户表的数据
    :param user: 注册用户的实例对象
    :return: 关联到用户的确认码
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_sha256(user.username, now)
    Email_Confirmation_Code.objects.create(code=code, user=user)
    return code


def send_register_mail(email,
                       code,
                       email_host_user=settings.EMAIL_HOST_USER,
                       site_ip=settings.SITE_IP,
                       confirm_days=settings.CONFIRM_DAYS):
    """
    * 发送用户注册确认邮件
    :param email: 用户注册邮箱
    :param code: 加密后的 sha256 哈希值
    """
    subject = 'Huaji Blog 的注册确认邮件'

    text_content = '''感谢您注册 Huaji Blog _(:з)∠)_ ,如果看到此条信息，说明您的邮箱可能没有开启 html 显示，或者不支持 html 内容显示。'''

    html_content = '''<h1>欢迎来到 Huaji Blog _(:з)∠)_</h1><br>
    <b>点击右侧链接即可完成注册：</b><a href="http://{}/account/register_confirm/?code={}" style="color: red;"> 点我点我</a><br>
    <b>此链接有效期{}天，注意及时验证</b>
    '''.format(site_ip, code, confirm_days)

    msg = EmailMultiAlternatives(subject, text_content, email_host_user, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
