from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.name

class Subset(models.Model) :
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.name

class Product(models.Model):
    subset = models.ForeignKey(Subset , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    #likes = models.ManyToManyField(User , blank=True , related_name="like")
    picture = models.ImageField()
    
    def __str__(self) :
        return self.name