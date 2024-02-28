from django.db import models
from django.contrib.auth.models import User
# from django.urls import reverse
# Create your models here.



class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=300)
    options=(
        ('Wood','Wood'),
        ('Metal','Metal'),
        ('Fabric','Fabric'),
        ('Paper','Paper'),
        ('Leather','Leather'),
        ('Cloth','Cloth'),
        ('Recycled Meterials','Recycled Meterials'),
        ('Other','Other'),

    )
    Meterial=models.CharField(max_length=100,choices=options,default='Wood')
    option=(
        ('Jwaleries','Jwaleirs'),
        ('Home Decor','Home Decor'),
        ('Statue','Statue'),
        ('Art Prints','Art Prints'),
        ('Stationary','Stationary'),
        ('Kitchen','Kitchen'),
        ('Other','Other'),
    )
    Type=models.CharField(max_length=100,choices=option,default='Wood')
    image=models.ImageField(upload_to="Product_images")

    def __str__(self):
        return self.name



class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(default='cart',max_length=100)



class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500,null=True)
    phone=models.IntegerField(null=True)
    option=(
        ('Pending','Pending'),
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=option,default="Order Placed")
