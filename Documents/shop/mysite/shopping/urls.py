from django.urls import path
from . import views

app_name = "shopping"

urlpatterns = [
    # 必須機能
    path('', views.index),
    # path('search/',views.search),
    path("serch/",views.serch),
    # path('item/<int:item_id>/', views.item_detail),
    path("item/<int:item_id>/",views.item_detail),
    # path('addToCart/',views.add_to_cart),
    path("addToCart/",views.add_to_cart),
    # path('cart/',views.cart),
    path("cart/",views.cart),

]