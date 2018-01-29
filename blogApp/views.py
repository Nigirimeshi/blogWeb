from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from commentApp.forms import CommentForm
from .models import Post, Category, Tag
import markdown
from blogProject import markdownnify


def index(request):
    """首页"""
    post_list = Post.objects.all()
    post_list = paging_index(request, post_list)

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def detail(request, post_pk):
    """文章详情页"""
    post = get_object_or_404(Post, pk=post_pk)
    # post.body = markdown.markdown(post.body, ['extra', 'codehilite', 'toc'])
    post.body = markdownnify.markdownify(post.body)

    # 获得这篇文章下的所有评论
    comment_list = post.comment_set.all().order_by('-created_time')

    # 引入"comment"数据模型的表单类的实例
    form = CommentForm()

    # 访问文章，阅读数+1
    post.increase_views()

    context = {'post': post,
               'comment_list': comment_list,
               'form': form,
               }
    return render(request, 'blogApp/detail.html', context)


def archives(request, year, month):
    """按归档日期显示文章"""
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month)
    post_list = paging_index(request, post_list)

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def category(request, cate_pk):
    """根据分类显示文章"""
    cate = get_object_or_404(Category, pk=cate_pk)
    post_list = Post.objects.filter(category=cate)
    post_list = paging_index(request, post_list)

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def tags(request, tag_pk):
    """根据标签显示文章"""
    t = get_object_or_404(Tag, pk=tag_pk)
    post_list = Post.objects.filter(tag=t)
    post_list = paging_index(request, post_list)

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def author(request, user_pk):
    """根据作者显示文章"""
    user = get_object_or_404(User, pk=user_pk)
    post_list = Post.objects.filter(author=user)
    post_list = paging_index(request, post_list)

    context = {'post_list': post_list}
    return render(request, 'blogApp/index.html', context)


def paging_index(request, post_list):
    """实现 index页面内的分页效果"""
    paginator = Paginator(post_list, 2)  # 每页显示两篇文章
    page = request.GET.get('page', 1)  # 用 GET 获取请求页码，默认为第一页
    try:
        post_list = paginator.page(page)  # 获取请求页内容
    except PageNotAnInteger:
        post_list = paginator.page(1)  # 请求页非整数，则显示第一页
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)  # 请求页超出了最大的页数，则显示最后一页
    return post_list
