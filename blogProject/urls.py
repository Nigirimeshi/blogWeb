"""blogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from blogApp.RSS import RssFeed
from blogApp.views import page_not_found

urlpatterns = [
    url(r'^sudoadmin/', admin.site.urls),
    # url(r'^markdownx/', include('markdownx.urls')),
    url(r'', include('ckeditor_uploader.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/', include('usersApp.urls')),
    url(r'', include('blogApp.urls', namespace='blogApp')),
    url(r'', include('commentApp.urls', namespace='commentApp')),
    url(r'^RSS/$', RssFeed(), name='RSS'),
    url(r'^search/', include('haystack.urls')),

    # 上述 include 实际包含的 urls
    # url(r'^account/login/$', views.login, name='login'),
    # url(r'^account/logout/$', views.logout, name='logout'),
    # url(r'^account/password_change/$', views.password_change, name='password_change'),
    # url(r'^account/password_change/done/$', views.password_change_done, name='password_change_done'),
    # url(r'^account/password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^account/password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    # url(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^account/reset/done/$', views.password_reset_complete, name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
