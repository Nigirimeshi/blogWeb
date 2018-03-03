from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    """分类数据库"""
    name = models.CharField(max_length=100, verbose_name="分类名")

    class Meta():
        verbose_name = verbose_name_plural = "文章分类"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签数据库"""
    name = models.CharField(max_length=100, verbose_name="标签名")

    class Meta():
        verbose_name = verbose_name_plural = "文章标签"

    def __str__(self):
        return self.name


class Post(models.Model):
    """文章数据库"""
    title = models.CharField(max_length=70, verbose_name="标题")
    body = RichTextUploadingField(verbose_name="正文")
    created_time = models.DateTimeField(verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    excerpt = models.CharField(max_length=200, blank=True, verbose_name="摘要")
    views = models.PositiveIntegerField(default=0, verbose_name="阅读量")
    # 外键约束
    category = models.ForeignKey(Category,null=True, blank=True, on_delete=models.SET_NULL, verbose_name="分类")
    tag = models.ManyToManyField(Tag, blank=True, verbose_name="标签")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="作者")

    class Meta():
        ordering = ['-created_time']
        verbose_name = verbose_name_plural = "文章"

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
            self.excerpt = strip_tags(self.body)[:140]
        super(Post, self).save(*args, **kwargs)
