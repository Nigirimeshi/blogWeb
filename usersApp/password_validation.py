from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class NumericPasswordValidator(object):
    """
    Validate whether the password is alphanumeric.
    自定义密码数字验证
    """
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("密码不能全部由数字组成。"),
                code='password_entirely_numeric',
            )

    def get_help_text(self):
        return _("Your password can't be entirely numeric.")