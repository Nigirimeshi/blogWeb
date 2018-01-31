from ..models import Category, Tag, Post
from django import template
from django.db.models.aggregates import Count

register = template.Library()


@register.simple_tag
def get_recent_post(num=5):
    """获取最新的5篇文章"""
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def get_archives():
    """获取文章创建时间,精确到月份,倒序"""
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    """获取所有文章分类"""
    return Category.objects.annotate(count_posts=Count('post')).filter(count_posts__gt=0)


@register.simple_tag
def get_tags():
    """获取所有标签"""
    return Tag.objects.annotate(count_posts=Count('post')).filter(count_posts__gt=0)
