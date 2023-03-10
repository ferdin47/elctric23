from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from product.models import Product
#from product.forms import ProductForm

def show(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def home(request):
    return render(request,"index.html" )
def about(request):
    return render(request,"about.html" )
def project(request):
    return render(request,"project.html" )
def testimonial(request):
    return render(request,"testimonial.html" )
def contact(request):
    return render(request,"contact.html" )

