from django.contrib import admin

from shop_app.models import Product, ProductMyOrder, MyOrder

# Register your models here.

admin.site.register(Product)
admin.site.register(MyOrder)
admin.site.register(ProductMyOrder)