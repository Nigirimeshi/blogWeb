from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from commentApp.forms import CommentForm
from .models import Post, Category, Tag
import markdown


def index(request):
    """首页"""
    post_list = Post.objects.all()

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def detail(request, post_pk):
    """文章详情页"""
    post = get_object_or_404(Post, pk=post_pk)
    post.body = markdown.markdown(post.body, ['extra', 'codehilite', 'toc'])

    # 获得这篇文章下的所有评论
    comment_list = post.comment_set.all().order_by('-created_time')

    # 引入"comment"数据模型的表单类的实例
    form = CommentForm()

    context = {'post': post,
               'comment_list': comment_list,
               'form': form,
               }
    return render(request, 'blogApp/detail.html', context)


def archives(request, year, month):
    """按归档日期显示文章"""
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def category(request, cate_pk):
    """根据分类显示文章"""
    cate = get_object_or_404(Category, pk=cate_pk)
    post_list = Post.objects.filter(category=cate)
    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def tags(request, tag_pk):
    """根据标签显示文章"""
    t = get_object_or_404(Tag, pk=tag_pk)
    post_list = Post.objects.filter(tag=t)
    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def author(request, user_pk):
    """根据作者显示文章"""
    user = get_object_or_404(User, pk=user_pk)
    post_list = Post.objects.filter(author=user)
    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)
