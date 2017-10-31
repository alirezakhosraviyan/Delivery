from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30, blank=True)
    Family = models.CharField(max_length=30, blank=True)
    Credit = models.IntegerField(default=0)

    def __str__(self):
        return "{}  {}".format(self.Name, self.Family)


class Category(models.Model):
    Name = models.CharField(max_length=30, blank=True)
    Detail = models.TextField(max_length=200)


class Product(models.Model):
    Name = models.CharField(max_length=30, blank=True)
    Family = models.CharField(max_length=30, blank=True)
    Price = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Detail = models.TextField(max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Payment(models.Model):
    Type = models.CharField(max_length=30, blank=True)
    Date = models.DateTimeField()
    Amount = models.IntegerField(default=0)
    Payer = models.ForeignKey(User,on_delete=models.CASCADE)

class Basket(models.Model):
    BasketId = models.IntegerField(auto_created=True)


class PeoductOfBasket(models.Model):
    Quantity = models.IntegerField(default=0)
    Basket = models.ForeignKey(Basket,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)





class Order(models.Model):
    Status = models.CharField(max_length=30,blank=True)
    Discount = models.IntegerField(default=0)
    TotalPrice = models.IntegerField(default=0)
    Address = models.TextField(max_length=100)
    User = models.ForeignKey(User ,on_delete=models.CASCADE)
    Basket = models.ForeignKey(Basket,on_delete=models.CASCADE)


class PreOrder(models.Model):
    Status = models.CharField(max_length=30,blank=True)
    Discount = models.IntegerField(default=0)
    TotalPrice = models.IntegerField(default=0)
    Address = models.TextField(max_length=100)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    Date = models.DateField()


class Comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Text = models.TextField(max_length=200)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Rating = models.IntegerField()
