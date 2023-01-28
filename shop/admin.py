from django.contrib import admin

# Register your models here.
from .models import Product, Orders, Contact, OrderUpdate

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Contact)
admin.site.register(OrderUpdate)


