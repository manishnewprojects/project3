from django.urls import path

from . import views
 

urlpatterns = [
    #path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('logged_out', views.logged_out, name='logged_out'),
     
]
