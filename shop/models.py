from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=12,
                                decimal_places=2,
                                validators=[MinValueValidator(0.01)])
    stock = models.PositiveIntegerField()
    listing_date = models.DateField(auto_now_add=True)

class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product,related_name='cart')

