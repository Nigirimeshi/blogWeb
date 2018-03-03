from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import User


class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        # help_text=_("Enter the same password as before, for verification."),
    )

    # def clean_email(self):
    #     """
    #     自定义处理表单字段
    #     """
    #     cleaned_data = self.cleaned_data['email']
    #     if len(cleaned_data) < 3:
    #         raise forms.ValidationError("太短了，不是邮箱！")
    #
    #     return None

    class Meta(UserCreationForm.Meta):
        model = User  # 指定的是自定义的用户模型 - usersApp.User
        fields = ('username', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

        # labels = {}

        # help_texts = {
        #     'username': _(''),
        # }

        # error_messages = {
        #     'password2': {
        #         'password_entirely_numeric': _("密码不能全为数字。"),
        #     },
        # }
        #
        # field_classes = {}



