from enum import auto
from django.db import models

# Create your models here.

class Items(models.Model):
    Name = models.CharField(max_length=100)
    Cat = [
        ('Phones','Phones'),
        ('Accessories','Accessories'),
        ('Sneakers','Sneakers'),
        ('Others','Others'),
    ]
    Category = models.CharField(max_length=50, choices=Cat)
    Description = models.CharField(max_length=500)
    Location = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Image = models.ImageField(upload_to = 'products')
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def phonecat(self):
        return self.Category == "Phones"
        
    def cat1(self):
        return self.Category == "Accessories"
    
    def cat2(self):
        return self.Category == "Sneakers"
    
    def cat3(self):
        return self.Category == "Others"
    
    
class OrderItem(models.Model):
    Item = models.ForeignKey(Items,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Product_name = models.CharField(max_length=100)
    Phone_num = models.CharField(max_length=15)
    Quantity = models.PositiveIntegerField(default=1)
    Address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
    
