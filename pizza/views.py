from django.shortcuts import render
from orders.models import Food_item, Cart, Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter  


def index(request):
	
	return render(request, 'home.html',
		{
 		'regular_pizza_list':Regular_Pizza.objects.all(), 
		'sicilian_pizza_list':Sicilian_Pizza.objects.all(),
		'topping_list':Topping.objects.all(),
		'subs_list': Sub.objects.all(),
		'pasta_list': Pasta.objects.all(),
		'salads_list': Salad.objects.all(),
		'dinner_list':  Dinner_Platter.objects.all(),

		}
	)
 