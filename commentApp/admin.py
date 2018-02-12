from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'text']
    fields = ['name', ('email', 'url'), 'text']
    date_hierarchy = 'created_time'


admin.site.register(Comment, CommentAdmin)
