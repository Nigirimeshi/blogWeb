from django.shortcuts import render, get_object_or_404, redirect
from blogApp.models import Post

from .models import Comment
from .forms import CommentForm


def comment_post(request, post_pk):
    """处理提交的评论表单数据"""
    # 文章pk存在的话，则生成该文章的实例
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        # 用请求的POST生成表单实例
        form = CommentForm(request.POST)
        # 表单数据合法则执行
        if form.is_valid():
            # 用表单的数据生成评论模型类的实例，但不保存到数据库
            comment = form.save(commit=False)
            # 关联评论与文章
            comment.post = post
            comment.save()
            # 当重定向到一个模型类的实例时会自动调用该模型实例的get_absolute_url()方法
            return redirect(post)
        else:
            # 获得该文章所有的评论
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list,
                       }
            return render(request, 'blogApp/detail.html', context)
    # 不是POST请求，说明没有提交数据，直接重定向到文章详情页
    else:
        redirect(post)
