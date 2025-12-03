from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *
from django.contrib import messages
from .form import CustomUserForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    #return HttpResponse("Welcome to the Food Bazaar!")
    category=Category.objects.filter(status=0)
    return render(request,"shop/index.html",{"category":category})

def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success ...")
            return redirect('/login/')
    return render(request,"shop/register.html",{'form':form})



def login_page(request):
    if request.user.is_authenticated:
        messages.success(request,"Already user is logged in")
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login/")
    return render(request,"shop/login.html")


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")
    return redirect("/")

def collections(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"shop/products/product.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect('home')
    
def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Produtct Found")
            return redirect('home')
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect('home')




   