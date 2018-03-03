from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

import pymysql

# 这确保应用程序 App 始终在 Django 启动时被导入，以便 shared_task 将来使用这个应用程序。
__all__ = ['celery_app']

# pymysql 取代 mysqldb
pymysql.install_as_MySQLdb()
