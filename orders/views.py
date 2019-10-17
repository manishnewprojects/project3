from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from .models import Food_item, Order, Cart, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http.request import QueryDict, MultiValueDict
import ast, datetime


#from cart.cart import Cart
 

@login_required
def place_order(request):
	return render(request, 'place_order.html',
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

def logged_out(request):
    return render(request, 'logged_out.html')

def online_access(request):
    return render(request, 'online_access.html')



def view_order(request):
	total=0
	cart = Cart.objects.filter(user = request.user)
	for citem in cart:
		total += citem.price
	return render(request, 'order_review.html', {'cart_list': cart, 'cart_total': total})

def final_order(request):
	total=0
	my_user = User.objects.get(username = request.user)

	order=Order.objects.create(user = my_user, time_placed="1999-01-01 12:12", total_price=0)
	f_item=Food_item.objects.create()
 
	cart = Cart.objects.filter(user = my_user)

	for citem in cart:
		f_item=Food_item.objects.create()

		total += citem.price
		f_item.item = citem.item
		f_item.price = citem.price
		f_item.save()
		print("fitem", f_item)
		order.food.add(f_item)

	order.total_price = total 
	print("food", order.food.all(), "OFRDE", order)
	order.save()
	cart.delete()

	return render(request, 'thanks.html', {'final_order':order, 'final_food_list':order.food.all() })


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
