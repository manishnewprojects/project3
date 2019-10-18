from django.contrib import admin

from .models import Food_item, Order, Cart, Regular_Pizza, Sicilian_Pizza, Topping, Sub, Salad, Pasta, Dinner_Platter 

admin.site.register(Cart)
admin.site.register(Food_item)
 
 
admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Topping)
admin.site.register(Salad)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Dinner_Platter)


class OrderAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['user', 'time_placed', 'order', 'total_price']

    def order(self, obj):
    	 
    	return([a.item for a in obj.food.all()])
 
admin.site.register(Order, OrderAdmin)