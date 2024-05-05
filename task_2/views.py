from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Client, Product, Order


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'task_2/client.html', {'clients': clients})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'task_2/product.html', {'products': products})

def order_list(request):
    current_date = timezone.now().date()
    period = request.GET.get('period')
    if period == 'week':
        start_date = current_date - timedelta(days=7)
    elif period == 'month':
        start_date = current_date - timedelta(days=30)
    elif period == 'year':
        start_date = current_date - timedelta(days=365)
    else:
        start_date = None

    if start_date:
        orders = Order.objects.filter(order_date__gte=start_date)
    else:
        orders = Order.objects.all()
    return render(request, 'task_2/orders.html', {'orders': orders})


def add_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        client, created = Client.objects.get_or_create(name="Anonymous", email="anonymous@example.com")
        order = Order.objects.create(client=client, total_amount=0)
        order.products.add(product)
        order.total_amount += product.price
        order.save()
        return redirect('task_2:order_list')
    else:
        return HttpResponseRedirect(reverse('task_2:product_list'))


