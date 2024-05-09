from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='task_2'

urlpatterns = [
    path('clients/', views.client_list, name='client_list'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('add/', views.add_product, name='add'),
]

