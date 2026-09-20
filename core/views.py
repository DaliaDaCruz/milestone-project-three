from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('request_list')
    else:
        form = ServiceRequestForm(instance=service_req)
    return render(request, 'core/request_form.html', {'form': form, 'title': 'Edit Repair Request'})

# 4. DELETE: Remove request
def request_delete(request, pk):
    service_req = get_object_or_404(ServiceRequest, pk=pk)
    if request.method == 'POST':
        service_req.delete()
        return redirect('request_list')
    return render(request, 'core/request_confirm_delete.html', {'request_item': service_req})