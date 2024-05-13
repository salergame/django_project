from django.contrib import admin

from task_2.models import Client, Order, Product

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = [
        "name",
        "email",
        "phone_number",
        "address",
        "registration_date",
    ]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","quantity","price"]
    list_editable = ["price",'quantity']
    search_fields = ["name","description"]
    list_filter = ["quantity","price"]
    fields = [
        "name",
        "description",
        "price",
        "quantity",
        "added_date",
    ]
    


@admin.register(Order)
class PaymentAdmin(admin.ModelAdmin):
    fields = [
        "client",
        "products",
        "total_amount",
        "order_date",
    ]


