from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import InnerUserManager
from app.settings import USER_TYPE_USER, USER_TYPE_ADMIN, USER_TYPE_MANAGER
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=False, blank=False, max_length=100, default='', unique=True,
                              verbose_name='Email')
    phone = models.CharField(max_length=11)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    type_of = models.IntegerField(default=USER_TYPE_USER)
    rate = models.ForeignKey('Rate', to_field='id', default='', null=True, db_column='rate_id', on_delete=models.CASCADE,
                             unique=False, verbose_name='Rate')
    objects = InnerUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        unique_together = ('email', 'phone')

class Device(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey('User', related_name='client',to_field='id', db_column='user_id', max_length=255,
		on_delete=models.CASCADE, blank=False, null=False, unique=False, verbose_name='User')
    ip_addr = models.CharField(max_length=15)

    class Meta:
        db_table = 'devices'

class Rate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rate'
