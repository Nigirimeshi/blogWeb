from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import CommentForm


@require_POST
def submit_comment(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        # print('success valid')
        comment = form.save(commit=False)
        comment.user = request.user
        comment.username = request.user.username
        comment.save()
        new_comment_location = "#c" + str(comment.id)
        json_content = {'msg': 'comment success!',
                        'new_comment_location': new_comment_location,
                        }
        return JsonResponse(json_content)
    json_content = {'msg': 'comment field!'}
    return JsonResponse(json_content)
