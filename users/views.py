from django.shortcuts import render , redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .form import Profill , Chats
from .models import Acount , Chat
from ghoghnoos.models import Order , Colors
import jdatetime
from django.contrib.auth.models import User
from django.db.models import Q , Count
# Create your views here.
def register(request) :
    if request.method != "POST" :
        form = UserCreationForm()
    else :
        form = UserCreationForm(data = request.POST)
        if form.is_valid() :
            new_user = form.save()
            login(request ,new_user)
            return redirect("ghoghnoos:index")
        
    context ={"form" : form}
    return render(request ,"registration/register.html" , context)

def fill_profill(request , totall_price) :
    order = Order.objects.filter(user = request.user ,add_buy_page = True)
    for pro in order :
        if pro.product :
            color = Colors.objects.get(name_color = pro.color , product = pro.product)
        elif pro.special :
            color = Colors.objects.get(name_color = pro.color , special = pro.special)
        elif pro.discount :
            color = Colors.objects.get(name_color = pro.color , discount = pro.discount)
        color.count -= pro.count
        pro.add_buy_page = False
        pro.date_added = f"{jdatetime.datetime.now().strftime("%Y/%m/%d : %H")}"
        pro.buy_action = True
        pro.count_action += pro.count
        pro.count = 0
        color.save()
        pro.save()
    try :
        acount = Acount.objects.get(user = request.user)
    except Acount.DoesNotExist :
        acount = Acount(user = request.user)
    if request.method != "POST" :
        form = Profill(instance=acount)
    else :
        form = Profill(instance=acount , data=request.POST)
        if form.is_valid() :
            form.save()
            return redirect(f"https://zarinp.al/python_developer?amount={totall_price}")
    
    context = {"form" : form , "totall_price" : totall_price}
    return render(request , "registration/profill.html" , context)

def user_information(request , username) :
    user = User.objects.get(username = username)
    acount = Acount.objects.get(user = user)
    context = {"information" : acount}
    return render(request , "registration/user_information.html" , context)

def chat_admin_page(request , username) :
    user = User.objects.get(username = username)
    if request.method != "POST" :
        form = Chats()
    else :
        form = Chats(data=request.POST)
        if form.is_valid() :
            new_text = form.save(commit=False)
            new_text.sender = request.user
            new_text.receiver = user
            form.save()
            return redirect("users:chat_admin_page" , username = username)
    
    chats = Chat.objects.filter(sender = request.user , receiver = user) | Chat.objects.filter(sender = user , receiver = request.user)
    chats = chats.order_by("date_added")
    for chat in chats :
        if chat.receiver == request.user :
            chat.admin_read = True
            chat.save()
    context = {"chats" : chats , "form" : form , "userr" : user}
    return render(request , "registration/chat_admin_page.html" , context)

def list_chat_admin(request) :
    users = User.objects.exclude(is_superuser = True)
    users = users.annotate(unread_count = Count("sender" ,
    filter=Q(sender__receiver=request.user,
    sender__admin_read = False))).order_by("-unread_count")
    
    context = {"users" : users }
    return render(request , "registration/list_chat_admin.html" , context)

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
            return redirect("users:chat_page")
        
    chats = Chat.objects.filter(sender = request.user , receiver = admin) | Chat.objects.filter(sender = admin , receiver = request.user)
    chats = chats.order_by("date_added")
    for chat in chats :
        if chat.receiver == request.user :
            chat.user_read = True
            chat.save()
    context = {"chats" : chats , "form" : form}
    return render(request , "registration/chat_page.html" , context)