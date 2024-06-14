from django.db import models

# Create your models here.
class mobile(models.Model):
    title =models.CharField(max_length=30)
    price= models.IntegerField()
    model= models.CharField(max_length=20)
    description= models.CharField(max_length=50)
    
    
    
    def __str__(self):
        return self.title