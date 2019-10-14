from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter, Cart 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http.request import QueryDict, MultiValueDict
import ast


#from cart.cart import Cart
 

@login_required
def place_order(request):
	 
 
	return render(request, 'place_order.html',
		{
		'regular_pizza_list':Regular_Pizza.objects.all(), 
		'sicilian_pizza_list':Sicilian_Pizza.objects.all(),
		'topping_list':Topping.objects.all(),
		}
	)

def logged_out(request):
    return render(request, 'logged_out.html')

def online_access(request):
    return render(request, 'online_access.html')

def view_order(request):

	cart = Cart.objects.filter(user = request.user)
	print("CART==", cart)
	return render(request, 'order_review.html', {'cart_list': cart})

def add_to_cart(request):
	if request.method == 'POST':
		my_user = User.objects.get(username = request.user)
		order_dict=ast.literal_eval(json.dumps(request.POST))
		
		food=""
		price=-1
		for key, value in dict(order_dict).items():  # ---> dict(query_dict)
			price=-1
			if key.find("[food]") != -1:
				food=value 
			else:
				price=float(value)
			if price!=-1:
				cart = Cart(user = my_user, item = food, price = price)
				cart.save()
		return render(request, 'order_review.html', {'cart': cart})

def remove_from_cart(request, order_id):
    product = Product.objects.get(id=order_id)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request, 'cart.html', {'cart': Cart(request)})