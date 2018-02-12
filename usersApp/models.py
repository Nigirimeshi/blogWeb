from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(max_length=50, blank=True)


class Email_Confirmation_Code(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ':' + self.code

    class Meta:
        ordering = ['created_time']
        verbose_name = '邮箱确认码'
        verbose_name_plural = '邮箱确认码'