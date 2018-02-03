from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """生成评论表单映射，类似数据库ORM"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        # 指定表单对应的数据库模型
        model = Comment
        # 指定表单显示的字段

        fields = ['name', 'email', 'url', 'text']
