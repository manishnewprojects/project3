from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Food
from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Subs, Salads, Pasta, Dinner_Platters 


def home(request):
	reg_pizza 	   = Regular_Pizza.objects.all().values()
	reg_pizza_list = [entry for entry in reg_pizza]
 

	return render(request, 'home.html', {'regular_pizza':reg_pizza_list})

def logged_out(request):
    return render(request, 'logged_out.html')
 
 