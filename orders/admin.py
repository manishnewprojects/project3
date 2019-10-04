from django.contrib import admin

from .models import Food

admin.site.register(Food)
admin.site.register(Order)

admin.site.register(Regular_Pizza)
admin.site.register(Sicilian_Pizza)
admin.site.register(Topping)
admin.site.register(Salads)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Dinner_Platters)