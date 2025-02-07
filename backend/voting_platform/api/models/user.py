""" This module contains code for the user model """
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from authemail.models import EmailUserManager, EmailAbstractUser
import uuid
from django.core.validators import MinLengthValidator

#from django.contrib.auth.models import AbstractUser

class User(EmailAbstractUser, PermissionsMixin):
    """ A user class email functionalities """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    stage_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    type = models.CharField(max_length=255, default="user")
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True)
    profile_photo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    objects = EmailUserManager()
   
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def has_perms(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return True
