from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

from markdownx.models import MarkdownxField
from blogProject import markdownnify


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
    views = models.PositiveIntegerField(default=0)
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

    def increase_views(self):
        """访问一次文章页面，自动增加一次"""
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        """重写save方法"""
        if not self.excerpt:
            self.excerpt = strip_tags(markdownnify.markdownify(self.body))[:50]
        super(Post, self).save(*args, **kwargs)
