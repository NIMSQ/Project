from django.db import models
from datetime import datetime
class Product(models.Model):
    
    x= [
        ('phone','phone'),
        ('computer','computer')
        
        
        
    ]
    name = models.CharField(max_length=50)
    content = models.TextField(null=True, blank= True)
    price = models.DecimalField(max_digits = 5, decimal_places = 2, default= 10.0)
    image = models.ImageField(upload_to= 'photos/%y/%m/%d',default='photos/4/16/desert.jpeg', verbose_name= 'photo')
    active = models.BooleanField(default = True)
    category = models.CharField(max_length= 50, null=True, blank= True, choices= x)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

