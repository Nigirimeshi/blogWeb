from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Category, Tag, Post


class PostAdmin(MarkdownxModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    search_fields = ['title']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
