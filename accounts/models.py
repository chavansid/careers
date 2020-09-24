import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from accounts.UserManager import UserManager
from django.contrib.auth.models import PermissionsMixin
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
# Create your models here.

class User(AbstractBaseUser,PermissionsMixin):
    uuid            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email           = models.EmailField(verbose_name="email_address",max_length=300,unique=True)
    password        = models.CharField(max_length=200,verbose_name='password')
    name            = models.CharField(max_length=200)
    date_of_birth   = models.DateField(verbose_name='date_of_birth',blank=True,default=None,null=True)
    created_at      = models.DateTimeField(verbose_name="created_at",auto_now_add=True)
    updated_at      = models.DateTimeField(verbose_name="updated_at",auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email

   