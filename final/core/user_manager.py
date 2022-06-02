from django.contrib.auth.models import BaseUserManager
from app.settings import USER_TYPE_USER, USER_TYPE_ADMIN, USER_TYPE_MANAGER

class InnerUserManager(BaseUserManager):
	def create_user(self, email, password=None, user_type=USER_TYPE_USER):
		if not email:
			raise ValueError('User must have an email')

		user = self.model(
			email=email
		)

		user.type_of = USER_TYPE_USER
		user.set_password(password)
		user.save(using=self.db)

		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password)
		user.type_of = USER_TYPE_ADMIN
		user.is_superuser = True
		user.is_admin = True
		user.is_active = True
		user.save(using=self.db)

		return user
