from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter, Cart 
from django.contrib.auth.models import User

#from cart.cart import Cart


def home(request):
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

def logged_out(request):
    return render(request, 'logged_out.html')
 
def add_to_cart(request):
	if request.method == 'POST':
		my_user = User.objects.get(username = request.user)
		food = "test"
		price =5
		cart = Cart(user = my_user, title = food, price = price)
		print("cart===",cart)	
		cart.save()
		return render(request, 'home.html', {'cart': cart})

def remove_from_cart(request, order_id):
    product = Product.objects.get(id=order_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})