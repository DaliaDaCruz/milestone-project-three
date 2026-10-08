from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ServiceRequest 

def index_view(request):
    """Renders the full landing page with catalog and repair requests."""
    products = Product.objects.all()
    requests = ServiceRequest.objects.all()
    return render(request, 'core/index.html', {  
        'products': products,
        'requests': requests,
    })


def request_list(request):
    """Renders the service repair tickets list page."""
    requests = ServiceRequest.objects.all()
    return render(request, 'core/request_list.html', {'requests': requests}) 


def request_create(request):
    """Handles creating or submitting a new repair request."""
    if request.method == 'POST':
        messages.success(request, "Request created successfully!")
        return redirect('request_list')
    
    return render(request, 'core/request_form.html')


def request_update(request, pk):
    """Handles editing an existing repair request."""
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        messages.success(request, "Request updated successfully!")
        return redirect('request_list')
        
    return render(request, 'core/request_form.html', {'request_obj': service_request})


def request_delete(request, pk):
    """Handles deleting a repair request."""
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        service_request.delete()
        messages.success(request, "Request deleted successfully!")
        return redirect('request_list')
        
    return render(request, 'core/request_confirm_delete.html', {'request_obj': service_request})


def checkout_view(request):
    """Renders the checkout page and processes orders."""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        if 'basket' in request.session:
            del request.session['basket']
        messages.success(request, f"Thank you {full_name}, your order has been placed!")
        return redirect('index')  
    
    return render(request, 'core/checkout.html')