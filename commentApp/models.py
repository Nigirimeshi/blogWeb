from django.db import models


class Comment(models.Model):
    """评论信息数据库"""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    post = models.ForeignKey('blogApp.Post')

    def __str__(self):
        return self.text[:25]
