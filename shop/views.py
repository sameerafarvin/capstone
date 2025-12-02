from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *
from django.contrib import messages
from .form import CustomUserForm



# Create your views here.
def home(request):
    #return HttpResponse("Welcome to the Food Bazaar!")
    category=Category.objects.filter(status=0)
    return render(request,"shop/index.html",{"category":category})

def collectionsview(request,name):
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



def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success Please Login")
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})
   