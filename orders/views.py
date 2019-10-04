from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import Food


def home(request):
	food 	= Food.objects.all().values()
	 
 
	food_list = [entry for entry in food]
 

	return render(request, 'home.html', {'food_list':food_list})

def logged_out(request):
    return render(request, 'logged_out.html')
 
 