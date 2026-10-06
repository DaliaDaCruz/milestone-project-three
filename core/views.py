from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ServiceRequest
from .forms import ServiceRequestForm

# 1. READ: Display list of requests and products
def request_list(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    products = Product.objects.all()
    return render(request, 'core/request_list.html', {'requests': requests, 'products': products})

# 2. CREATE: Add new service request
def request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Service request submitted successfully!")
            return redirect('request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'core/request_form.html', {'form': form, 'title': 'Submit Repair Request'})

# 3. UPDATE: Edit existing request
def request_update(request, pk):
    service_req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_req)
        if form.is_valid():
            form.save()
            messages.success(request, "Service request updated!")
            return redirect('request_list')
    else:
        form = ServiceRequestForm(instance=service_req)
    return render(request, 'core/request_form.html', {'form': form, 'title': 'Edit Repair Request'})

# 4. DELETE: Remove request
def request_delete(request, pk):
    service_req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        service_req.delete()
        messages.success(request, "Service request deleted.")
        return redirect('request_list')
    return render(request, 'core/request_confirm_delete.html', {'request_item': service_req})

# 5. CHECKOUT: Handle basket and order placement
def checkout_view(request):
    basket = request.session.get('basket', {})

    if request.method == 'POST':
        request.session['basket'] = {}
        messages.success(request, "Thank you! Your order has been placed successfully.")
        return redirect('request_list')

    return render(request, 'core/checkout.html', {'basket': basket})