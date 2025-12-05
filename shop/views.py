from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
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
    
def add_to_cart(request):
    #print("POST data:", request.POST)

    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = request.POST.get('product_id')
            product_qty = int(request.POST.get('qty'))

            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                messages.error(request, f"No Such Product Found. Product ID: {product_id}")
                return redirect('home') 

            # check available stock
            if product.quantity >= product_qty:
                
                # check if product already in cart
                cart_item = Cart.objects.filter(user=request.user, product=product).first()

                if cart_item:
                    # REPLACE quantity instead of adding
                    cart_item.product_qty = product_qty
                    cart_item.save()
                    messages.success(request, "Cart quantity updated")
                    return redirect('cart')
                else:
                    # create new cart item
                    Cart.objects.create(
                        user=request.user,
                        product=product,
                        product_qty=product_qty
                    )
                    messages.success(request, "Product Added to Cart")
                    return redirect('cart')
            else:
                messages.error(request, f"Only {product.quantity} Quantity Available")
        else:
            messages.error(request, "Login to Continue")
    return redirect('/')


def cart_page(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request, "shop/cart.html", {"cart": cart})
    else:
        messages.error(request, "Login to Continue")
        return redirect('/login/')
    



   