from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from datetime import datetime
  
class Order(models.Model):
	user_rec    = models.ForeignKey(User, on_delete=models.CASCADE)
	time_placed   = models.DateTimeField(default=timezone.now)
	total_price = models.DecimalField(max_digits=5, decimal_places=2)
	time_done = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.total_price


class Cart(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	item = models.CharField(max_length = 100)
	price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	
	def __str__(self):
		return f"{self.title}, {self.price}"


class Regular_Pizza(models.Model):
	name        = models.CharField(max_length=40)
	sm_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	lg_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	extras		= models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
 
	def __str__(self):
		return f"{self.name}"

class Sicilian_Pizza(models.Model):
	name        = models.CharField(max_length=40)
	sm_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	lg_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	extras		= models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)

	def __str__(self):
		return f"{self.name}"


class Topping(models.Model):
	name        = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.name}"


class Sub(models.Model):
	name        = models.CharField(max_length=20)
	sm_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	lg_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
 
	def __str__(self):
		return f"{self.name},{self.sm_price},{self.lg_price} "

class Pasta(models.Model):
	name        = models.CharField(max_length=30)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.price}"

class Salad(models.Model):
	name        = models.CharField(max_length=20)
	price	    = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.price}"

class Dinner_Platter(models.Model):
	name        = models.CharField(max_length=20)
	sm_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
	lg_price	= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
 
	def __str__(self):
		return f"{self.name},{self.sm_price},{self.lg_price} "




		