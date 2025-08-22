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
            num2 = dis.price
            dis.percent = 100 - int((num2/num1)*100)
            dis.save()
        if dis.url_name == "-":
            dis.url_name = dis.name.replace(" ","-")
            dis.save()
    for spe in special :
        if spe.url_name == "-":
            spe.url_name = spe.name.replace(" " , "-")
            spe.save()
    for cate in category :
        if cate.url_name == "-" :
            cate.url_name = cate.name.replace(" " , "-")
            cate.save()
    context = {"discount" : discount , "category" : category , "special" : special}
    return render(request , "ghoghnoos/index.html", context)

def subset_list(request , category_name) :
    category = Category.objects.get(url_name = category_name)
    subset = category.subset_set.all()
    for sub in subset :
        if sub.url_name == "-":
            sub.url_name = sub.name.replace(" " , "-")
            sub.save()
    context = {"subset" : subset , "category_name" : category_name}
    return render(request , "ghoghnoos/subset_list.html" , context)

def product_list(request , category_name,subset_name) :
    subset = Subset.objects.get(url_name = subset_name)
    product = subset.product_set.all()
    for pro in product :
        if pro.url_name == "-":
            pro.url_name = pro.name.replace(" " , "-")
            pro.save()
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

def product(request , product_name) :
    try :
        product = Special.objects.get(url_name = product_name)
    except Special.DoesNotExist :
        try :
            product = Discount.objects.get(url_name = product_name)
        except Discount.DoesNotExist :
            product = Product.objects.get(url_name = product_name)
    context = {"product" : product}
    return render(request , "ghoghnoos/product.html" , context)
    
    