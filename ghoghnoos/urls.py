from django.urls import path
from . import views

app_name = "ghoghnoos"
urlpatterns = [
    path("" , views.index , name="index"),
    path("subset_list/<str:category_name>/" , views.subset_list , name="subset_list"),
    path("product_list/<str:category_name>/<str:subset_name>/" , views.product_list , name="product_list"),
    path("special_list/" , views.special_list , name="special_list"),
    path("discount_list/" , views.discount_list , name="discount_list"),
]