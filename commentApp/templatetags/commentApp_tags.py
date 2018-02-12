from django import template
from django.db.models.aggregates import Count

from ..forms import CommentForm


register = template.Library()

@register.simple_tag
def create_comment_form(post):
    form = CommentForm(initial={'post': post.pk})
    return form


@register.simple_tag
def get_comment_set(post):
    return post.comment_set.all()


@register.simple_tag
def get_comment_user_count(post):
    user_list = []
    for comment in post.comment_set.all():
        if not comment in user_list:
            user_list.append(comment)
    return len(user_list)
