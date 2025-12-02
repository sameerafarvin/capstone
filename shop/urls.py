from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:name>',views.collectionsview,name='home'),
    path('<str:cname>/<str:pname>',views.product_details,name="product_details"),
    path('register/', views.register, name='register'),
    
]