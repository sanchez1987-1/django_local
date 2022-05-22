from django.test import TestCase
from . import models
from test_django import settings as s

# Create your tests here.

class BookAuthorTestCase(TestCase):
	def test_author_book(self):
		u_a = models.User.objects.create(email='dvsdv@sfe.ru', phone='79154646',
			name='Test', surname='TestS', type_of=s.USER_TYPE_ADMIN)
		b = models.Book(name='Test Book 1', author=u_a)
		try:
			b.save()
		except ValueError as e:
			print("Falied to create book")
		else:
			self.fail('Falied with ValueError')