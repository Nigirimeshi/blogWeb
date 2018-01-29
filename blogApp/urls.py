from django.conf.urls import url
from . import views


app_name = 'blogApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/?page=[1-9][0-9]*', views.index, name='index'),
    url(r'^post/(?P<post_pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<cate_pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/(?P<tag_pk>[0-9]+)/$', views.tags, name='tags'),
    url(r'^author/(?P<user_pk>[0-9]+)/$', views.author, name='author'),
]