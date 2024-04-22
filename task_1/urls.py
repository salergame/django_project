from django.urls import path
from task_1 import views

app_name='task_1'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
