from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    # ('Stationary', 'Stationary'),
    # ('Electronics', 'Electronics'),
    # ('Food', 'Food'),
    #Updated code lines 
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Clothing', 'Clothing'),
    ('Cleaning Supplies', 'Cleaning Supplies'),
    ('Hardware and Tools', 'Hardware and Tools'),
    ('Home and Kitchen', 'Home and Kitchen'),
    ('Health and Beauty', 'Health and Beauty'),
    ('Sports and Outdoors', 'Sports and Outdoors'),
    ('Toys', 'Toys'),
    ('Pet Supplies', 'Pet Supplies'),
    ('Accessories', 'Accessories'),
    ('Medical Supplies', 'Medical Supplies'),
    ('Gardening Supplies', 'Gardening Supplies'),
    ('Baby Products', 'Baby Products'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category=models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        #return f'{self.name}-{self.quantity}'
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'




