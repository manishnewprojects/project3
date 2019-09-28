from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    
    path('login', auth_views.login, name='login'),
    path('logout', auth_views.logout, {'next_page': 'logged_out'}, name='logout'),

    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),

]

 