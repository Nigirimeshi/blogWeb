from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Comment


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'url', 'text']
#     fields = ['name', ('email', 'url'), 'text']
#     date_hierarchy = 'created_time'


admin.site.register(Comment, MPTTModelAdmin)
