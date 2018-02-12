from django.conf.urls import url
from . import views


app_name = 'commentApp'

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)', views.submit_comment, name='submit_comment'),
]