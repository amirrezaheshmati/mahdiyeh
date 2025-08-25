from django.urls import path , include
from . import views

app_name = "users"
urlpatterns  = [
    path("" , include("django.contrib.auth.urls")) ,
    path("register/" , views.register , name="register"),
    path("register_invite/<str:user_up>/" , views.register_invite , name="register_invite"),
    path("informations/<int:totall_price>/" , views.fill_profill , name="profill"),
    path("user_information/<str:username>/" , views.user_information , name="user_information"),
    path("chat_page/" , views.chat_user_page , name="chat_page"),
    path("list_chat_admin/" , views.list_chat_admin , name="list_chat_admin"),
    path("chat_admin_page/<str:username>/" , views.chat_admin_page , name="chat_admin_page"),
    path("percents_page/" , views.user_percents , name="percents_page"),
    path("user_invite/<str:user_up>/<str:user_owner>/" , views.user_invite , name="user_invite")
]