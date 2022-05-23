from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import InnerUserManager
from test_django.settings import USER_TYPE_USER, USER_TYPE_ADMIN, USER_TYPE_AUTHOR

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=255)
	author = models.ForeignKey('User', related_name='author',to_field='id', db_column='user_id', max_length=255,
		on_delete=models.CASCADE, blank=False, null=False, unique=False, verbose_name='fio')
	linked_by = models.ManyToManyField('User', through='BookUsers')

	@property	
	def likes(self):
		res = [b.user.email for b in BookUsers.objects.filter(book_id=self.id)]
		return res

	def save(self, *args, **kwargs):
		if self.author.type_of != USER_TYPE_AUTHOR:
			raise ValueError("Only author.")
		return super(Book, self).save(*args, **kwargs)

	class Meta:
		db_table = 'books'

class User(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(null=False, blank=False, max_length=100, default='', unique=True,
								verbose_name='Email')
	phone = models.CharField(max_length=11)
	is_staff = models.BooleanField(default=False)
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	type_of = models.IntegerField(default=USER_TYPE_USER)

	objects = InnerUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	class Meta:
		db_table = 'users'
		unique_together = ('email','phone')

class BookUsers(models.Model):
	user = models.ForeignKey('User', to_field='id', db_column='user_id', on_delete=models.CASCADE, 
		blank=False, null=False, unique=False)
	book = models.ForeignKey('Book', to_field='id', db_column='book_id', on_delete=models.CASCADE,
		blank=False, null=False, unique=False, verbose_name='fio')

	def __str__(self):
		return f'{self.user.name} like {self.book.name}'

	class Meta:
		db_table = 'user_books_favorites'
			