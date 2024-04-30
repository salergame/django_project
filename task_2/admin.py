from django.contrib import admin

from task_2.models import Client, Order, Product

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)

