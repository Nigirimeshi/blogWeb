from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.utils.text import slugify

from commentApp.forms import CommentForm
from .models import Post, Category, Tag
# from markdown.extensions.toc import TocExtension
import markdown
# from blogProject import markdownnify
from markdownx.utils import markdownify


def index(request):
    """首页"""
    post_list = Post.objects.all()
    context_data = paging_index(request, post_list)

    context = context_data
    return render(request, 'blogApp/index.html', context)


def detail(request, post_pk):
    """文章详情页"""
    post = get_object_or_404(Post, pk=post_pk)
    # post.body = markdown.markdown(post.body, ['extra', 'codehilite', 'toc'])
    # post.body = markdownify(post.body)
    md = markdown.Markdown(extensions=[
        'extra',
        'codehilite',
        'toc',
        # TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

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
    context_data = paging_index(request, post_list)

    context = context_data
    return render(request, 'blogApp/index.html', context)


def category(request, cate_pk):
    """根据分类显示文章"""
    cate = get_object_or_404(Category, pk=cate_pk)
    post_list = Post.objects.filter(category=cate)
    context_data = paging_index(request, post_list)

    context = context_data
    return render(request, 'blogApp/index.html', context)


def tags(request, tag_pk):
    """根据标签显示文章"""
    t = get_object_or_404(Tag, pk=tag_pk)
    post_list = Post.objects.filter(tag=t)
    context_data = paging_index(request, post_list)

    context = context_data
    return render(request, 'blogApp/index.html', context)


def author(request, user_pk):
    """根据作者显示文章"""
    user = get_object_or_404(User, pk=user_pk)
    post_list = Post.objects.filter(author=user)
    context_data = paging_index(request, post_list)

    context = context_data
    return render(request, 'blogApp/index.html', context)


def about(request):
    context = {}
    return render(request, 'blogApp/about.html', context)


def timeline(request):
    year = Post.objects.dates('created_time', 'year', order='DESC')
    month = Post.objects.dates('created_time', 'month', order='DESC')
    post_list = Post.objects.all()
    context = {'year': year,
               'month': month,
               'post_list': post_list,
               }
    return render(request, 'blogApp/timeline.html', context)


def paging_index(request, post_list):
    """
    * 实现 index页面内的分页效果
    * 效果如： 1 .. 2 3 4 5 6 7 8 .. 100
    """
    per_page_size = 5
    paginator = Paginator(post_list, per_page_size)  # 每页显示的文章数量

    # 文章总数少于每页显示的文章数量，则不分页
    if paginator.count <= per_page_size:
        context_data = {'post_list': post_list}
        return context_data

    page_number = int(request.GET.get('page', 1))  # 用 GET 获取当前请求页码，默认为第一页

    left = []  # 当前页左侧连续页码号
    right = []  # 当前页右侧连续页码号
    left_show_more = False  # 第1页页码号后面是否显示省略号
    right_show_more = False  # 最后一页页码号前面是否显示省略号
    first_page = False  # 是否显示第1页页码号，如果 left 中包含 1，则不显示
    last_page = False  # 是否显示最后一页页码号，如果 right 中包含最后一页的页码，则不显示

    total_pages = paginator.num_pages  # 分页后的总页数
    page_range = paginator.page_range  # 获取分页后所有页码组成的列表，如 [1, 2, 3, 4, 5]

    if page_number == 1:
        # 请求第1页，则 left 连续页码号不需要页码列表，因此默认 left = []
        # right 需要页码列表，如 right = [2, 3, 4]
        # + 3 可改，已显示更多页码，就算超出总页数，也不会报错，只会取到列表最后一位，同 [page_number:-1]
        right = page_range[page_number:page_number + 3]

        if right[-1] < total_pages - 1:
            # 如果"右侧连续页码号"最后一位页码比"分页后总页数"减 1 后还要小，说明他们之间还有其他页，需要显示省略号
            right_show_more = True
        if right[-1] < total_pages:
            # 如果 right 最后一位比"总页数"小，则需要显示最后一页
            last_page = True

    elif page_number == total_pages:
        # 如果请求最后一页，则 right 就不需要页码列表，因此默认 right = []
        # left 需要页码列表，如 left = [2, 3, 4]
        # -4 可改，获取了最后一页前连续的 3 个页码，不足 3 页，则从第一页开始
        left = page_range[(page_number - 4) if (page_number - 4) > 0 else 0:page_number - 1]

        if left[0] > 2:
            # 如果 left 最左边页码比第二页要大，说明他们之间还有其他页，需要显示省略号
            left_show_more = True

        if left[0] > 1:
            # 如果 left 最左边页码比第一页要大，说明 left 不包含第一页，需要显示第一页
            first_page = True

    else:
        # 如果请求的非第一页和最后一页，则 left 和 right 都需要页码列表
        left = page_range[(page_number - 4) if (page_number - 4) > 0 else 0:page_number - 1]
        right = page_range[page_number:page_number + 3]

        if left[0] > 2:
            left_show_more = True
        if left[0] > 1:
            first_page = True

        if right[-1] < total_pages - 1:
            right_show_more = True
        if right[-1] < total_pages:
            last_page = True

    try:
        post_list = paginator.page(page_number)  # 获取请求页内容
    except PageNotAnInteger:
        post_list = paginator.page(1)  # 请求页非整数，则显示第一页
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)  # 请求页超出了最大的页数，则显示最后一页

    context_data = {'left': left,
                    'right': right,
                    'left_show_more': left_show_more,
                    'right_show_more': right_show_more,
                    'first_page': first_page,
                    'last_page': last_page,
                    'post_list': post_list,
                    }
    return context_data


def page_not_found(request):
    return render(request, '404.html')
