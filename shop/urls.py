from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('cart/',views.cart_page, name="cart"),
    path('addtocart/',views.add_to_cart,name="addtocart"),
    # dynamic url routing
    path('<str:name>/',views.collections,name='product'),
    path('<str:cname>/<str:pname>/',views.product_details,name="product_details"),
   
    
]