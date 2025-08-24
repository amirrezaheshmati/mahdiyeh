from django.shortcuts import render ,get_object_or_404, redirect
from django.db.models import Q , Count
from .form import CommentAdded , ReplayAdded , AddToBuyPage , AddProduct  , Chats
from .models import Product , Comments , Order , Chat , ChatUser , User
from random import choice
import jdatetime
from users.models import Acount
from django.contrib.auth.decorators import user_passes_test
# Create your views here.
def index(request) :
    return render(request , "shopping/index.html")

def product_list(request) :
    product = Product.objects.all()
    context = {"product" : product}
    return render(request , "shopping/product_list.html" , context)
    
def product_describe(request , product_id) :
    product = Product.objects.get(id = product_id)
    try :
        order = Order.objects.get(user = request.user,
                                  product = product)
    except Order.DoesNotExist :
        order = Order(user = request.user , 
                      product = product)
    if request.method != "POST" :
        form = AddToBuyPage(instance=order)
    else :
        form = AddToBuyPage(instance=order, data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect("shopping:product_describe" , product_id = product_id)

    context = {"form" : form , "product" : product , "pro_ord" : order}
    return render(request , "shopping/product_describe.html" , context)

def comments(request , product_id) :
    product = Product.objects.get(id = product_id)
    comments = product.comments_set.order_by("date_added")
    context = {"product" : product , "comments" : comments}
    return render(request , "shopping/comments.html" , context)

def add_comment(request , product_id) :
    product = Product.objects.get(id = product_id)
    if request.method != "POST" :
        form = CommentAdded()
    else :
        form = CommentAdded(data=request.POST)
        if form.is_valid() :
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.product = product
            new_comment.save()
            return redirect("shopping:comments" , product_id = product_id)
    
    context = {"form" : form , "product" : product}
    return render(request , "shopping/add_comment.html" , context)

def add_replay(request , comment_id , product_id) :
    product = Product.objects.get(id = product_id)
    comment = Comments.objects.get(id = comment_id)
    if request.method != "POST" :
        form = ReplayAdded()
    else :
        form = ReplayAdded(data=request.POST)
        if form.is_valid() :
            new_replay = form.save(commit=False)
            new_replay.comment = comment
            new_replay.user = request.user
            new_replay.save()
            return redirect("shopping:comments" ,product_id = product_id )
    
    context = {"form" : form , "comment" : comment , "product" : product}
    return render(request , "shopping/add_replay.html" , context)


def buy_page(request) :
    return render(request , "shopping/buy_page.html")

def buy_list(request) :
    order = Order.objects.filter(user = request.user ,count__gt = 0)
    totall_price = 0
    for pro in order :
        pro.level1 = True
        totall_price += pro.count * pro.product.price
        pro.save()
    context = {"order" : order , "totall_price" : totall_price}
    return render(request , "shopping/buy_list.html" , context)

def buy_action(request) :
    numbers = list(n for n in range(10))
    order = Order.objects.filter(user = request.user , level2 = True)
    revieve_code = ""
    for x in range(8) :
        num = choice(numbers)
        revieve_code += str(num)
    for pro in order :
        if pro.recieve_code == 0 :
            pro.recieve_code = revieve_code
            pro.date_added = f"{jdatetime.datetime.now().strftime("%Y/%m/%d : %H")}"
            pro.shows = 1
            pro.save()
    context = {"order" : order}
    return render(request , "shopping/buy_action.html" , context)

def delete_user(request , product_id) :
    order = Order.objects.get(id = product_id)
    if request.method != "POST" :
        order.level2 = False
        order.level3 = True
        order.shows = 3
        order.date_deleted= f"{jdatetime.datetime.now().strftime("%Y/%m/%d : %H")}"
        order.save()
        return redirect("shopping:buy_page")

def buy_history(request) :
    order = Order.objects.order_by("-date_deleted").filter(user = request.user , level3 = True)
    context = {"order" : order}
    return render(request , "shopping/buy_history.html" , context)

def is_admin(user) :
    return user.is_superuser

@user_passes_test(is_admin)
def admin_panel(request) :
    if request.method != "POST" :
        form = AddProduct()
    else :
        form = AddProduct(request.POST , request.FILES)
        if form.is_valid() :
            form.save()
            return redirect("shopping:product_list")

    context = {"form" : form}
    return render(request , "shopping/admin_panel.html" , context)
    
def admin_action(request) :
    acount = Acount.objects.all()
    order = Order.objects.order_by( "shows","-date_added").filter(level2 = True)
    context = {"order" : order , "acount" : acount}
    return render(request , "shopping/admin_action.html" , context)

def admin_history(request) :
    acount = Acount.objects.all()
    order = Order.objects.order_by("-date_deleted").filter(level3 = True)
    context = {"acount" : acount , "order" : order}
    return render(request , "shopping/admin_history.html" , context)

def delete_admin_product(request , product_id) :
    order = Order.objects.get(id = product_id)
    if request.method != "POST" :
        order.level3 = False
        order.level2 = True
        order.shows = 3
        order.save()
    return render(request , "shopping/index.html")

def like_post(request, post_id) :
    like = get_object_or_404(Product , id = post_id)
    if request.user in like.likes.all() :
        like.likes.remove(request.user)
    else :
        like.likes.add(request.user)
        
    return redirect("shopping:product_list")

def like_comment(request , comment_id , product_id) :
    like = get_object_or_404(Comments , id = comment_id)
    product = get_object_or_404(Product , id = product_id)
    if request.user in like.likes.all() :
        like.likes.remove(request.user)
    else :
        like.likes.add(request.user)

    return redirect("shopping:comments" , product_id = product_id)

def supporting_page(request) :
    return render(request , "shopping/supporting_page.html")

def chat_user_page(request) :
    admin = User.objects.get(is_superuser = True)
    if request.method != "POST" :
        form = Chats()
    else :
        form = Chats(data=request.POST) 
        if form.is_valid() :
            new_text = form.save(commit=False)
            new_text.sender = request.user
            new_text.receiver = admin
            form.save()
            return redirect("shopping:chat_page")
        
    chats = Chat.objects.filter(sender = request.user , receiver = admin) | Chat.objects.filter(sender = admin , receiver = request.user)
    chats = chats.order_by("date_added")
    for chat in chats :
        if chat.receiver == request.user :
            chat.user_read = True
            chat.save()
    context = {"chats" : chats , "form" : form}
    return render(request , "shopping/chat_page.html" , context)

def list_chat_admin(request) :
    users = User.objects.exclude(is_superuser = True)
    users = users.annotate(unread_count = Count("sender" ,
    filter=Q(sender__receiver=request.user,
    sender__admin_read = False))).order_by("-unread_count")
    
    context = {"users" : users }
    return render(request , "shopping/list_chat_admin.html" , context)

def chat_admin_page(request , user_id) :
    user = User.objects.get(id = user_id)
    if request.method != "POST" :
        form = Chats()
    else :
        form = Chats(data=request.POST)
        if form.is_valid() :
            new_text = form.save(commit=False)
            new_text.sender = request.user
            new_text.receiver = user
            form.save()
            return redirect("shopping:chat_admin_page" , user_id = user_id)
    
    chats = Chat.objects.filter(sender = request.user , receiver = user) | Chat.objects.filter(sender = user , receiver = request.user)
    chats = chats.order_by("date_added")
    for chat in chats :
        if chat.receiver == request.user :
            chat.admin_read = True
            chat.save()
    context = {"chats" : chats , "form" : form , "userr" : user}
    return render(request , "shopping/chat_admin_page.html" , context)