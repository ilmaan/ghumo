from django.db import models

# Create your models here.


class Destin(models.Model):
    
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    dsc = models.TextField()
    price = models.IntegerField()
    ofr = models.BooleanField(default=False)



