from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """生成评论表单映射，类似数据库ORM"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'http://'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '抢沙发，抢地板 _(:з)∠)_'}))


    class Meta:
        # 指定表单对应的数据库模型
        model = Comment
        # 指定表单显示的字段
        fields = ['name', 'email', 'url', 'text']

        # widgets= {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '抢沙发，抢地板 _(:з)∠)_'}),
        # }

        labels = {}

        help_texts = {}

        error_messages = {}

        field_classes = {}
