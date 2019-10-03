from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Order(models.Model):
	user_rec    = models.ForeignKey(User, on_delete=models.CASCADE)
	time_placed   = models.DateTimeField(default=timezone.now)
	total_price = models.DecimalField(max_digits=5, decimal_places=2)
	time_done = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.total_price


class Regular_Pizza(models.Model):
	name        = models.CharField(max_length=20)
	size		= models.CharField(max_length=3, blank=True)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.size} {self.price}"


class Sicilian_Pizza(models.Model):
	name        = models.CharField(max_length=20)
	size		= models.CharField(max_length=3, blank=True)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.size} {self.price}"


class Topping(models.Model):
	name        = models.CharField(max_length=20)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.price}"


class Subs(models.Model):
	name        = models.CharField(max_length=20)
	size		= models.CharField(max_length=3, blank=True)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.size} {self.price}"

class Pasta(models.Model):
	name        = models.CharField(max_length=20)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.price}"

class Salads(models.Model):
	name        = models.CharField(max_length=20)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.price}"

class Dinner_Platters(models.Model):
	name        = models.CharField(max_length=20)
	size		= models.CharField(max_length=3, blank=True)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.size} {self.price}"
