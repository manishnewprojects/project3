from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class order(models.Model):
	user_rec    = models.ForeignKey(User, on_delete=models.CASCADE)
	time_placed   = models.DateTimeField(default=timezone.now)
	total_price = models.DecimalField(max_digits=5, decimal_places=2)
	time_done = models.DateTimeField(default=timezone.now, blank=True, null=True)

	def __str__(self):
		return self.total_price


class food(models.Model):
	name        = models.CharField(max_length=20)
	food_type   = models.CharField(max_length=40)
	size	    = models.CharField(max_length=3)
	price	    = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return self.name

	def get_total_cost(self):
		return self.price


class toppings(models.Model):
	topping_type  = models.CharField(max_length=40)
	topping_price = models.DecimalField(max_digits=3, decimal_places=2)

	def __str__(self):
		return self.topping_type

