from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)', views.comment_post, name='comment'),
]