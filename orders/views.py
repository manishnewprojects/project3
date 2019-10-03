from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Subs, Salads, Pasta, Dinner_Platters 

 

def home(request):
	regular_pizza 	= Regular_Pizza.objects.all().values()
	sicilian_pizza 	= Sicilian_Pizza.objects.all()
	toppings 		= Topping.objects.all()
	subs 			= Subs.objects.all()
	salads			= Salads.objects.all()
	pastas 			= Pasta.objects.all()
	dinner_platters = Dinner_Platters.objects.all()
	print("reg", regular_pizza)
 
	pizza_list = [entry for entry in regular_pizza]
	pizza_list2 = list(regular_pizza)

	food_list = {
	'regular_pizza':pizza_list2,
	}

	return render(request, 'home.html', {'regular_pizzas':regular_pizza})

def logged_out(request):
    return render(request, 'logged_out.html')
 
 