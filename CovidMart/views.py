from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def login_view(request):
    return render(request, 'login.html')

def cart_view(request):
    return render(request, 'cart.html')
    
def produce_view(request):
    return render(request, 'produce.html')