from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=15,verbose_name='Номер телефона')
    address = models.CharField(max_length=255,verbose_name="Адрес")
    registration_date = models.DateField(auto_now_add=True,verbose_name="Дата регистраций")

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цен")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    added_date = models.DateField(auto_now_add=True,verbose_name="Дата")

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE,verbose_name="Клиент")
    products = models.ManyToManyField(Product,verbose_name="Продукт")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Общая сумма")
    order_date = models.DateField(auto_now_add=True,verbose_name="Дата заказа")
    
    def __str__(self):
        return f"Заказ {self.id} клиент: {self.client.name}"
