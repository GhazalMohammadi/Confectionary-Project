from django.contrib import admin
from .models import City , CategoriesOfProducts , Product , Warehouse , Inventory , Order , OrderItem
# Register your models here.
admin.site.register(City)
admin.site.register(CategoriesOfProducts)
admin.site.register(Product)
admin.site.register(Warehouse)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(OrderItem)
