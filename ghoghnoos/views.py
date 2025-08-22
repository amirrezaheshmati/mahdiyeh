from django.shortcuts import render
from .models import Product , Category , Subset , Discount , Special
# Create your views here.

def index(request):
    special = Special.objects.all()
    discount = Discount.objects.all()
    category = Category.objects.all()
    for dis in discount :
        if dis.percent == 0:
            num1 = dis.price1
            num2 = dis.price2
            dis.percent = 100 - int((num2/num1)*100)
        dis.save()
    context = {"discount" : discount , "category" : category , "special" : special}
    return render(request , "ghoghnoos/index.html", context)

def subset_list(request , category_name) :
    category = Category.objects.get(name = category_name)
    subset = category.subset_set.all()
    context = {"subset" : subset , "category_name" : category_name}
    return render(request , "ghoghnoos/subset_list.html" , context)

def product_list(request , category_name,subset_name) :
    subset = Subset.objects.get(name = subset_name)
    product = subset.product_set.all()
    context = {"product" : product}
    return render(request , "ghoghnoos/product_list.html" , context)

def special_list(request) :
    special = Special.objects.all()
    context = {"special" : special}
    return render(request , "ghoghnoos/special_list.html" , context)

def discount_list(request) :
    discount = Discount.objects.all()
    context = {"discount" : discount}
    return render(request , "ghoghnoos/discount_list.html" , context)