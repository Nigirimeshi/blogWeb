from django.core.mail import EmailMultiAlternatives
from blogProject import settings, celery_app


@celery_app.task
def send_register_mail(email,
                       code,
                       email_host_user=settings.EMAIL_HOST_USER,
                       site_ip=settings.SITE_IP,
                       confirm_days=settings.CONFIRM_DAYS):
    """
    发送用户注册认证邮件

    :param email: 用户注册邮箱
    :param code: 加密后的 sha256 哈希值
    :param email_host_user: 用来发送邮件的邮箱地址
    :param site_ip: 网站地址
    :param confirm_days: 认证有效时间

    """
    subject = 'Huaji Blog 的注册认证邮件'

    text_content = '''感谢您注册 Huaji Blog _(:з)∠)_ ,如果看到此条信息，说明您的邮箱可能没有开启 html 显示，或者不支持 html 内容显示。'''

    html_content = '''<h1>欢迎来到 Huaji Blog _(:з)∠)_</h1><br>
    <b>点击右侧链接即可完成注册：</b><a href="http://{}/account/register_confirm/?code={}" style="color: red;"> 点我点我</a><br>
    <b>此链接有效期{}天，注意及时验证</b>
    '''.format(site_ip, code, confirm_days)

    msg = EmailMultiAlternatives(subject, text_content, email_host_user, [email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    print("已成功发送邮件！")
