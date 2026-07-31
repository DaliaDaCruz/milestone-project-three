from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def catalog(request):
    return render(request, 'core/cataloge.html')

def booking(request):
    return render(request, 'core/booking.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')