"""from django.contrib import admin
from .models import User
from authemail.admin import EmailUserAdmin
from django.contrib.auth import get_user_model


class CustomUserAdmin(EmailUserAdmin):
    model = User
    list_filter = ["is_staff"]

admin.site.unregister(get_user_model())
admin.site.register(User, CustomUserAdmin)"""
