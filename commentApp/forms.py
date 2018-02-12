from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
<<<<<<< HEAD
=======
    """生成评论表单映射，类似数据库ORM"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
>>>>>>> eae28d47ba32e265defa9514129416545354dcf4

    class Meta:
        model = Comment
<<<<<<< HEAD
        fields = ('content', 'parent', 'post')

=======
        # 指定表单显示的字段

        fields = ['name', 'email', 'url', 'text']
>>>>>>> eae28d47ba32e265defa9514129416545354dcf4
