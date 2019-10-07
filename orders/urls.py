from django.urls import path

from . import views
 

urlpatterns = [

    path('home', views.home, name='home'),

    path('logged_out', views.logged_out, name='logged_out'),
 
 	path('add_to_cart', views.add_to_cart, name='add_to_cart'),

]
