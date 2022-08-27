import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '测试邮件', '1325274460@qq.com', 'pikeduo@gmail.com'
    text_content = '你好！'
    html_content = '<p>欢迎访问<a href="http://localhost:8000/login/" target=blank>http://localhost:8000/login/</a>你好!</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()