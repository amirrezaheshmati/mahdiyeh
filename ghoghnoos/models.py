from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=20)
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return self.name

class Subset(models.Model) :
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return self.name

class Product(models.Model):
    subset = models.ForeignKey(Subset , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    #likes = models.ManyToManyField(User , blank=True , related_name="like")
    picture = models.ImageField()
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return self.name

class Special(models.Model) :
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    picture = models.ImageField()
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return self.name

class Discount(models.Model) :
    name = models.CharField(max_length=20)
    price1 = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    percent = models.IntegerField(default=0)
    picture = models.ImageField()
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return f"{self.name} => {self.percent}"
    
class Order(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    special = models.ForeignKey(Special , on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date_sended = models.CharField()
    count = models.PositiveIntegerField(default=0)
    receive_code = models.PositiveBigIntegerField(default=0)
    