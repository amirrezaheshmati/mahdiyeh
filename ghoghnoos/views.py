from django.shortcuts import render , redirect
from .models import Product , Category , Subset , Discount , Special 
from .form import AddProduct , AddCategory , AddSubset , AddColor , AddSize , OrderForm , AddSpecial , AddDiscount , OrderForm2
# Create your views here.

def index(request):
    special = Special.objects.all()
    discount = Discount.objects.all()
    category = Category.objects.all()
    context = {"discount" : discount , "category" : category , "special" : special}
    return render(request , "ghoghnoos/index.html", context)

def subset_list(request , category_name) :
    category = Category.objects.get(url_name = category_name)
    subset = category.subset_set.all()
    context = {"subset" : subset , "category_name" : category.name}
    return render(request , "ghoghnoos/subset_list.html" , context)

def product_list(request , category_name,subset_name) :
    subset = Subset.objects.get(url_name = subset_name)
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

def product(request , product_name) :
    try :
        product = Special.objects.get(url_name = product_name)
    except Special.DoesNotExist :
        try :
            product = Discount.objects.get(url_name = product_name)
        except Discount.DoesNotExist :
            product = Product.objects.get(url_name = product_name)
    
    if request.method != "POST" :
        form = OrderForm(product = product)
        form2 = OrderForm2()
    else :
        form = OrderForm(request.POST , product = product)
        form2 = OrderForm2(data=request.POST)
        if form.is_valid() :
            selected_color = form.cleaned_data["color"]
            return redirect("ghoghnoos:index")
    
    context = {"product" : product , "form" : form , "form2" : form2}
    return render(request , "ghoghnoos/product.html" , context)

def add_product(request , category_name , subset_url) :
    category = Category.objects.get(name = category_name)
    subset = Subset.objects.get(url_name = subset_url , category = category)
    product = subset.product_set.all()
    if request.method != "POST" :
        form = AddProduct()
    else :
        form = AddProduct(request.POST , request.FILES)
        if form.is_valid() :
            new_product = form.save(commit=False)
            new_product.subset = subset
            new_product.url_name = new_product.name.replace(" " , "-")
            new_product.save()
            return redirect("ghoghnoos:edit_product" , product_url = new_product.url_name)
    
    context = {"form" : form , "category" : category , "subset" : subset}
    return render(request , "ghoghnoos/add_product.html" , context)

def admin_panel(request) :
    return render(request , "ghoghnoos/admin_panel.html")

def add_category(request) :
    category = Category.objects.all()
    if request.method != "POST" :
        form = AddCategory()
    else :
        form = AddCategory(data=request.POST)
        if form.is_valid() :
            new_category = form.save(commit=False)
            new_category.url_name = new_category.name.replace(" " , "-")
            new_category.save()
            return redirect("ghoghnoos:add_category")
    context = {"category" : category , "form" : form}
    return render(request , "ghoghnoos/add_category.html" , context)

def add_subset(request , category_name) :
    category = Category.objects.get(url_name = category_name)
    subset = category.subset_set.all()
    if request.method != "POST" :
        form = AddSubset()
    else :
        form = AddSubset(data=request.POST)
        if form.is_valid() :
            new_subset = form.save(commit=False)
            new_subset.category = category
            new_subset.url_name = new_subset.name.replace(" " , "-")
            new_subset.save()
            return redirect("ghoghnoos:add_subset" , category_name = category_name)
    
    context = {"form" : form , "category" : category , "subset" : subset}
    return render(request , "ghoghnoos/add_subset.html" , context)

def edit_product(request , product_url) :
    special = False
    discount = False
    pro = False
    try :
        product = Special.objects.get(url_name = product_url)
        special = True
    except Special.DoesNotExist :
        try :
            product = Discount.objects.get(url_name = product_url)
            discount = True
        except Discount.DoesNotExist :
            product = Product.objects.get(url_name = product_url)
            pro = True
    color = product.colors_set.all()
    size = product.size_set.all()
    
    if request.method != "POST":
        if pro :
            form_product = AddProduct(instance= product)
        elif special :
            form_product = AddSpecial(instance= product)
        elif discount :
            form_product = AddDiscount(instance= product)
        form_color = AddColor()
        form_size = AddSize()
    else :
        form_color = AddColor(data=request.POST)
        form_size = AddSize(data=request.POST)
        if pro :
            form_product = AddProduct(request.POST , request.FILES , instance=product )
        elif special :
            form_product = AddSpecial(request.POST , request.FILES , instance=product)
        elif discount :
            form_product = AddDiscount(request.POST , request.FILES , instance=product)
        if form_color.is_valid and form_size.is_valid() and form_product.is_valid() :
            new_product = form_product.save(commit=False)
            new_color = form_color.save(commit=False)
            new_size = form_size.save(commit=False)
            if pro :
                new_color.product = product
                new_size.product = product
            elif discount :
                num1 = new_product.price1
                num2 = new_product.price
                new_product.percent = 100 - int((num2/num1)*100)
                new_color.discount = product
                new_size.discount = product
                #num1 = new_product.price1
                #num2 = new_product.price
                #new_product.percent = 100 - int((num2/num1)*100)
            elif special :
                new_color.special = product
                new_size.special = product
            if new_color.name_color :
                new_color.save()
            if new_size.height and new_size.width and new_size.colm :
                new_size.save()
            new_product.save()
            return redirect("ghoghnoos:edit_product" , product_url = product_url)
    
    context = {"product" : product , "form_product" : form_product, "size" : size ,
            "form_color" : form_color , "form_size" : form_size , "color" : color}
    return render(request , "ghoghnoos/edit_product.html" , context)

def all_products(request) :
    products = Product.objects.all()
    context = {"product" : products}
    return render(request , "ghoghnoos/all_products.html" , context)

def add_special(request) :
    if request.method != "POST" :
        form = AddSpecial()
    else :
        form = AddSpecial(request.POST , request.FILES)
        if form.is_valid() :
            new_special = form.save(commit=False)
            new_special.url_name = new_special.name.replace(" " , "-")
            new_special.save()
            return redirect("ghoghnoos:edit_product" , product_url = new_special.url_name)
    
    context = {"form" : form}
    return render(request , "ghoghnoos/add_special.html", context)

def add_discount(request) :
    if request.method != "POST" :
        form = AddDiscount()
    else :
        form = AddDiscount(request.POST , request.FILES)
        if form.is_valid() :
            new_discount = form.save(commit=False)
            new_discount.url_name = new_discount.name.replace(" " , "-")
            num1 = new_discount.price1
            num2 = new_discount.price
            new_discount.percent = 100 - int((num2/num1)*100)
            new_discount.save()
            return redirect("ghoghnoos:edit_product" , product_url = new_discount.url_name)
    
    context = {"form" : form}
    return render(request , "ghoghnoos/add_discount.html" , context)