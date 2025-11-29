from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from django.contrib import messages


# Create your views here.
def home(request):
    #return HttpResponse("Welcome to the Food Bazaar!")
    category=Category.objects.filter(status=0)
    return render(request,"shop/index.html",{"category":category})
    


def register(request):
    return render(request, 'shop/register.html')
   