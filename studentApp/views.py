from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def error_404(request):
    return render(request, '404.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def register_owner(request):
    return render(request, 'register-owner.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def mess(request):
    return render(request, 'mess.html')

def pg(request):
    return render(request, 'pg.html')

def about(request):
    return render(request, 'about.html')

def viewdetails(request):
    return render(request, 'viewdetails.html')