from django.urls import path
from . import views

app_name='task_2'

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
]
