from django.shortcuts import render
from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Subs, Salads, Pasta, Dinner_Platters 

 

def home(request):
	regular_pizza 	= Regular_Pizza.objects.all()
	sicilian_pizza 	= Sicilian_Pizza.objects.all()
	toppings 		= Topping.objects.all()
	subs 			= Subs.objects.all()
	salads			= Salads.objects.all()
	pastas 			= Pasta.objects.all()
	dinner_platters = Dinner_Platters.objects.all()
	food_list = {

	'regular_pizza':regular_pizza,



	}

	return render(request, 'home.html', {'regular_pizzas':regular_pizza})

def logged_out(request):
    return render(request, 'logged_out.html')
 


