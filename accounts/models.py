import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from accounts.UserManager import UserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
# Create your models here.

class BaseModel(models.Model):
    uuid            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at      = models.DateTimeField(verbose_name="created_at",auto_now_add=True)
    updated_at      = models.DateTimeField(verbose_name="updated_at",auto_now=True)
    
    class Meta:
        abstract = True

class User(BaseModel,AbstractBaseUser,PermissionsMixin):
    email           = models.EmailField(verbose_name="email_address",max_length=300,unique=True)
    password        = models.CharField(max_length=200,verbose_name='password')
    name            = models.CharField(max_length=200)
    date_of_birth   = models.DateField(verbose_name='date_of_birth',blank=True,default=None,null=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(BaseModel):
    user               = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    selfie_image       = models.ImageField(default='default.png',upload_to='profile_pics',null=True)
    bio                = models.CharField(default=None,max_length=500,null=True)
    headline           = models.CharField(default=None,max_length=100,null=True)

    def __str__(self):
        return f'{self.user.email}'

class Education(BaseModel):
    pass

class Experience(BaseModel):
    pass