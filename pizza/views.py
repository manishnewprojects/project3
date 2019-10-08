from django.shortcuts import render
from orders.models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter, Cart 


def index(request):
	reg_pizza 	   			= Regular_Pizza.objects.all().values()
	reg_pizza_list 			= [entry for entry in reg_pizza]

	sicilian_pizza 			= Sicilian_Pizza.objects.all().values()
	sicilian_pizza_list 	= [entry for entry in sicilian_pizza]
 
	topping 				= Topping.objects.all().values()
	topping_list 			= [entry for entry in topping]
 
	return render(request, 'home.html',
		{
		'regular_pizza_list':reg_pizza_list, 
		'sicilian_pizza_list':sicilian_pizza_list,
		'topping_list':topping_list,
		}
	)
 