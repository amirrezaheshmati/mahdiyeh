from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model) :
    name = models.CharField(max_length=20)
    url_name = models.CharField(max_length=20 , default="-")
    picture = models.ImageField()
    
    def __str__(self) :
        return self.name

class Subset(models.Model) :
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url_name = models.CharField(max_length=20 , default="-")
    picture = models.ImageField()
    
    def __str__(self) :
        return self.name


class Product(models.Model):
    subset = models.ForeignKey(Subset , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    totall_price = models.PositiveBigIntegerField(default=0)
    likes = models.ManyToManyField(User , blank=True , related_name="like_pro")
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    
    def __str__(self) :
        return self.name

class Special(models.Model) :
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    totall_price = models.PositiveBigIntegerField(default=0)
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    likes = models.ManyToManyField(User , blank=True , related_name="like_special") 
    
    def __str__(self) :
        return self.name

class Discount(models.Model) :
    name = models.CharField(max_length=20)
    price1 = models.PositiveBigIntegerField()
    price = models.PositiveBigIntegerField()
    totall_price = models.PositiveBigIntegerField(default=0)
    percent = models.IntegerField(default=0)
    describe = models.TextField()
    url_name = models.CharField(max_length=20 , default="-")
    likes = models.ManyToManyField(User , blank=True , related_name="like_discount")
    
    def __str__(self) :
        return f"{self.name} => {self.percent}"
    
class Pictures(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True , related_name="product_image")
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE , blank=True , null=True , related_name="discount_image")
    special = models.ForeignKey(Special , on_delete=models.CASCADE , blank=True , null=True , related_name="special_image")
    picture = models.ImageField(blank=True , null=True)

class Comments(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE , blank=True  , null=True)
    special = models.ForeignKey(Special, on_delete=models.CASCADE , blank=True  , null=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE , blank=True  , null=True)
    text = models.TextField()
    likes = models.ManyToManyField(User , blank=True , related_name="like_commnet")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.text[:50]}..."

class Colors(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True)
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE , blank=True , null=True)
    special = models.ForeignKey(Special , on_delete=models.CASCADE , blank=True , null=True)
    name_color = models.CharField(max_length=20 , blank=True , null=True)
    price_color = models.PositiveBigIntegerField( blank=True , null=True)
    count = models.PositiveSmallIntegerField(blank=True , null=True)

    def __str__(self):
        if self.name_color :
            return self.name_color
    
class Size(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True)
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE , blank=True , null=True)
    special = models.ForeignKey(Special , on_delete=models.CASCADE , blank=True , null=True)
    height = models.IntegerField( blank=True , null=True)
    width = models.IntegerField(blank=True , null=True)
    colm = models.IntegerField(blank=True , null=True)
    price_size = models.PositiveBigIntegerField(blank=True , null=True)
    
    def __str__(self):
        if self.height and self.width and self.colm :
            return f"{self.height}*{self.width}*{self.colm}"

class Order(models.Model) :
    product = models.ForeignKey(Product , on_delete=models.CASCADE , blank=True , null=True)
    discount = models.ForeignKey(Discount , on_delete=models.CASCADE , blank=True , null=True)
    special = models.ForeignKey(Special , on_delete=models.CASCADE , blank=True , null=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    describe = models.TextField(blank=True , null=True)
    color = models.CharField(blank=True , null=True)
    color_price = models.PositiveBigIntegerField(default=0)
    size = models.CharField(blank=True , null=True)
    size_price = models.PositiveBigIntegerField(default=0)
    date_sended = models.CharField(blank=True , null=True)
    date_added = models.CharField(blank=True , null=True)
    count = models.PositiveSmallIntegerField(null=True , blank=True)
    count_action = models.PositiveSmallIntegerField(default=0)
    count_history = models.PositiveSmallIntegerField(default=0)
    buy_action = models.BooleanField(default=False)
    buy_history = models.BooleanField(default=False)
    add_buy_page = models.BooleanField(default=False)

class TrackingCode(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True, blank=True)
    link = models.TextField()
    tracking_code = models.PositiveBigIntegerField()