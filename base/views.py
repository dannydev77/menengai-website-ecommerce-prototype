from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def about(request):
    return render(request, 'base/about.html')


def products(request):
    return render(request, 'base/products.html')


def product(request):
    return render(request, 'base/products.html')


def careers(request):
    return render(request, 'base/careers.html')



def users(request):
    return render(request, 'base/management.html')


def contact(request):
    return render(request, 'base/contact.html')

