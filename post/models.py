from django.db import models
#from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='post')
    
    
    def __str__ (self):
        return f"{self.name} - {self.price}"