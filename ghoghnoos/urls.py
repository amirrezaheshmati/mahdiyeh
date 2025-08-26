from django.urls import path
from . import views

app_name = "ghoghnoos"
urlpatterns = [
    path("" , views.index , name="index"),
    path("subset_list/<str:category_name>/" , views.subset_list , name="subset_list"),
    path("product_list/<str:category_name>/<str:subset_name>/" , views.product_list , name="product_list"),
    path("special_list/" , views.special_list , name="special_list"),
    path("discount_list/" , views.discount_list , name="discount_list"),
    path("product/<str:product_name>/" , views.product , name="product"),
    path("admin_panel/" , views.admin_panel , name="admin_panel"),
    path("add_category/" , views.add_category , name="add_category"),
    path("add_subset/<str:category_name>/" , views.add_subset , name="add_subset"),
    path("add_product/<str:category_name>/<str:subset_url>/" , views.add_product , name="add_product"),
    path("edit_product/<str:product_url>/" , views.edit_product , name="edit_product"),
    path("all_products/" , views.all_products , name="all_products"),
    path("add_special/" , views.add_special , name="add_special"),
    path("add_discount/" , views.add_discount , name="add_discount"),
    path("buy_page/" , views.buy_page , name="buy_page"),
    path("admin_action/" , views.admin_action , name="admin_action"),
    path("user_action/" , views.user_action , name="user_action"),
    path("action_list/<str:username>/" , views.action_list , name="action_list"),
    path("complite/<str:username>/" , views.complite_order , name="complite"),
    path("buy_history/" , views.buy_history , name="buy_history"),
    path("admin_history/" , views.admin_history , name="admin_history"),
    path("comment/<int:product_id>/" , views.comments , name="comments") , 
    path("add_comment/<int:product_id>/" , views.add_comment , name="add_comment"),
    path("add_replay/<int:product_id>/<int:comment_id>" , views.add_replay , name="add_replay"),
    path("like_post/<str:where>/<str:post_name>/" , views.like_post , name="like_post"),
    path("like_comment/<int:comment_id>/<int:product_id>/" , views.like_comment , name="like_comment"),
    path("search_result/" , views.search_product , name="search_result"),
]