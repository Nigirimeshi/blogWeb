from django.contrib import admin
from .models import User, Email_Confirmation_Code


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active']


admin.site.register(User, UserAdmin)
admin.site.register(Email_Confirmation_Code)

