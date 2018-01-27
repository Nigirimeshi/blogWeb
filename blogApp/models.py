from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from markdownx.models import MarkdownxField


class Category(models.Model):
    """分类数据库"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签数据库"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    title = models.CharField(max_length=70)
    body = MarkdownxField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    # 外键约束
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    class Meta():
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """解析视图对应的URL，并用对象pk替换正则匹配的post_pk部分"""
        return reverse('blogApp:detail', kwargs={'post_pk': self.pk})
