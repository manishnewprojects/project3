from django.contrib import admin

from .models import order, food, toppings

admin.site.register(order)
admin.site.register(food)
admin.site.register(toppings)

 