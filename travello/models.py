from django.db import models

# Create your models here.

class Destination(models.Model):
    name= models.CharField(max_length=80)
    description= models.TextField(max_length=100)
    price= models.IntegerField()
    img= models.ImageField(upload_to='pics')
    special_offer= models.BooleanField(default=False)