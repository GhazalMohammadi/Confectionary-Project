from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255 , unique=True)

    def __str__(self):
        return self.name
    
class CategoriesOfProducts(models.Model):
    name = models.CharField(max_length=255 , db_index =True)
    slug = models.SlugField(max_length = 255 , unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255 , db_index =True)
    slug = models.SlugField(max_length = 255 , unique=True)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits = 7 , decimal_places = 3)
    categories = models.ForeignKey(CategoriesOfProducts,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Warehouse(models.Model):
    name = models.CharField(max_length=255 , db_index =True)
    address = models.TextField()
    city = models.ForeignKey(City , on_delete=models.CASCADE)   
    def __str__(self):
        return self.name 


UNIT_CHOICES = (
    ('kilograms', 'KG'),
    ('grams', 'G'),
)
class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='kilograms')

    def get_absolute_url(self):
        return reverse('order',kwargs={'inventory_id':self.id})

    def get_add_to_cart_url(self):
        return reverse('addToCart',kwargs={'inventory_id':self.id})
    
    def get_remove_from_cart_url(self):
        return reverse('removeFromCart',kwargs={'inventory_id':self.id})

class OrderItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Inventory , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
