from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import TreeForeignKey, MPTTModel


class Comment(MPTTModel):
    """评论信息数据库"""
<<<<<<< HEAD
    username = models.CharField(max_length=150, verbose_name='用户名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    content = RichTextUploadingField(config_name='user')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(settings.COMMENT_BIND_MODEL, null=True, blank=True, on_delete=models.CASCADE, verbose_name='评论的文章')
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父级评论')


    class MPTTMeta:
        order_insertion_by = ['created_time']
=======
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    post = models.ForeignKey('blogApp.Post')
>>>>>>> eae28d47ba32e265defa9514129416545354dcf4

    def __str__(self):
        if self.parent is not None:
            return "%s 回复 %s" % (self.username, self.parent.username)
        return "%s 评论文章: %s" % (self.username, self.post.title)
