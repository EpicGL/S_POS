from email.policy import default
from django.db import models


class Product(models.Model):
    CATEGORY = (
                ('Burger', 'Burger'),
                ('Fried Chicken', 'Fried Chicken'),
                ('Beverage', 'Beverage'),
                ('Dessert', 'Dessert'),
               )
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices = CATEGORY)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='itemimg/',blank=True,null=True)

    def __str__(self):
        return str(self.title)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/itemimg/placehonder.jpg'
        return url 
