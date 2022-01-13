from django.contrib.auth import get_user_model
from django.db import models
import random
userinfo = get_user_model()


class Driver(models.Model):
	driver = models.OneToOneField(userinfo, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def str(self):
		return self.driver

	class Meta:
		verbose_name = 'driver'
		verbose_name_plural = 'drivers'


class Client(models.Model):
	client = models.OneToOneField(userinfo, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	def str(self):
		return self.client

	class Meta:
		verbose_name = 'client'
		verbose_name_plural = 'clients'

PAYMENT = (
    ('processing', 'processing'),
    ('click', 'click'),
    ('payme', 'payme'),
    ('cancelled', 'cancelled'),
)

Status = (
	('Created', 'Created'),
	('Cancelled', 'Cancelled'),
	('Accepted', 'Accepted'),
	('Finished', 'Finished'),
)


def create_new_ref_number():
	return str(random.randint(10000, 99999))


class Order(models.Model):
	order_id = models.CharField(max_length=10, blank=True,
								unique=True, default=create_new_ref_number())
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
	status = models.CharField(max_length=100, choices=Status, default='Created')
	pay = models.CharField(max_length=100, choices=PAYMENT, default='processing')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def str(self):
		return f'{self.client}, {self.driver}'

	class Meta:
		verbose_name = 'order'
		verbose_name_plural = 'orders'
