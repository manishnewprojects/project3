from django.urls import path

from . import views
 

urlpatterns = [

    path('logged_out', views.logged_out, name='logged_out'),
 
 	path('add_to_cart', views.add_to_cart, name='add_to_cart'),

 	path('online_access', views.online_access, name='online_access'),

 	path('place_order', views.place_order, name='place_order'),

    path('home', views.place_order, name='home'),

]
