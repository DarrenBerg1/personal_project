from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
    email = models.EmailField(max_length=200, null= False, blank=False, unique=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name} | {self.email}"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.price}"
    
class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    
class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=False)
    zipcode = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f"{self.address}"