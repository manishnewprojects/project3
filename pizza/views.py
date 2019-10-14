from django.shortcuts import render
from orders.models import Food, Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter, Cart 


def index(request):
	
	return render(request, 'home.html',
		{
		'pizza_list': Food.objects.filter(category__contains='pizza'),
		'regular_pizza_list':Regular_Pizza.objects.all(), 
		'sicilian_pizza_list':Sicilian_Pizza.objects.all(),
		'topping_list':Topping.objects.all(),
		}
	)
 