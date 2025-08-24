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
]