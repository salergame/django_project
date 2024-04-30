from django.shortcuts import render
from .models import Client, Product, Order


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'task_2/client.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'task_2/product.html', {'products': products})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'task_2/order.html', {'orders': orders})
