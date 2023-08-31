from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    # Other fields specific to the category

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=300)

    def __str__(self):
        return self.name
class Product (models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bar_code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Cart (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
         return f"CartItem for {self.cart.user.username}, Product: {self.product.name}"



