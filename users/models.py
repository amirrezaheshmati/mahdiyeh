from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Acount(models.Model) :
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    number_phone1 = models.BigIntegerField(max_length=11)
    number_phone2 = models.BigIntegerField(max_length=11)
    post_code = models.BigIntegerField()
    addres = models.TextField()
    
    def __str__(self):
        return self.name

class Chat(models.Model) :
    sender = models.ForeignKey(User , on_delete=models.CASCADE , related_name="sender")
    receiver = models.ForeignKey(User , on_delete=models.CASCADE , related_name="receiver")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    admin_read = models.BooleanField(default=False)
    user_read = models.BooleanField(default=False)