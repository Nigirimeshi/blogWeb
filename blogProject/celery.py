from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# 为 celery 程序设置默认的 Django 设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogProject.settings')

app = Celery('blogProject')

# 在这里使用字符串意味着工作人员不必序列化配置对象到子进程
# - namespace ='CELERY'表示所有与芹菜相关的配置密钥，都应该有一个`CELERY_`前缀。
app.config_from_object('django.conf:settings', namespace='CELERY')

# 从所有已注册的Django应用程序配置中加载任务模块。
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
