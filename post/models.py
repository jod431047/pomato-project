from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    image = models.ImageField(upload_to='post')
    
    
    def __str__ (self):
        return self.name