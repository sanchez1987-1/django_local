from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import InnerUserManager
from test_django.settings import USER_TYPE_USER, USER_TYPE_ADMIN, USER_TYPE_AUTHOR

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=255)
	author = models.CharField(max_length=255, verbose_name='fio', db_column='name_surname')
	
	class Meta:
		db_table = 'books'

class User(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(null=False, blank=False, max_length=100, default='', unique=True,
								verbose_name='Email')
	phone = models.CharField(max_length=11)
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	type_of = models.IntegerField(default=USER_TYPE_USER)

	objects = InnerUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		db_table = 'users'
		unique_together = ('email','phone')
