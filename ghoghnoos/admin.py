from django.contrib import admin

from .models import Product , Subset , Category , Discount , Special , Colors , Order , TrackingCode
# Register your models here.
admin.site.register(Category)
admin.site.register(Subset)
admin.site.register(Product)
admin.site.register(Discount)
admin.site.register(Special)
admin.site.register(Colors)
admin.site.register(Order)
admin.site.register(TrackingCode)