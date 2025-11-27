from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("Welcome to the Food Bazaar!")
    return render(request, 'shop/index.html')


def register(request):
    return render(request, 'shop/register.html')
   