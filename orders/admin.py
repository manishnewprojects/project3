from django.contrib import admin

from .models import Order, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter, Cart 

admin.site.register(Order)
admin.site.register(Cart)


admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Topping)
admin.site.register(Salad)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Dinner_Platter)