from django.shortcuts import render
from .models import ProductDetails
# Create your views here.

def home(request):
    return render (request,'home.html')


def UserDetails(request):
    product=ProductDetails.objects.all()
    return render(request,'User.html',{'product':product})