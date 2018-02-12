from django.conf.urls import url
from . import views


app_name = 'usersApp'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^register_confirm/', views.register_confirm, name='register_confirm'),
    url(r'^register/done/$', views.register_done, name='register_done'),
]