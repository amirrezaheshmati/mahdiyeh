from django.contrib import admin

from .models import Product , Subset , Category , Discount , Special
# Register your models here.
admin.site.register(Category)
admin.site.register(Subset)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Special)
