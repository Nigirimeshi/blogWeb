from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """生成评论表单映射，类似数据库ORM"""
    class Meta:
        # 指定表单对应的数据库模型
        model = Comment
        # 指定表单显示的字段
        fields = ['name', 'email', 'url', 'text']