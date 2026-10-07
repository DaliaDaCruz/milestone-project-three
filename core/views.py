from django.shortcuts import render, redirect
from django.contrib import messages

def request_list(request):
    """Renders the main product catalog/homepage."""
    return render(request, 'core/request_list.html') 

def request_create(request):
    """Handles creating or submitting a new request/order."""
    if request.method == 'POST':
        messages.success(request, "Request created successfully!")
        return redirect('request_list')
    
    return render(request, 'core/request_form.html')

def request_update(request, pk):
    return render(request, 'core/request_form.html')

def request_delete(request, pk):
    return render(request, 'core/request_confirm_delete.html')

def checkout_view(request):
    """Renders the checkout page."""
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        if 'basket' in request.session:
            del request.session['basket']
        messages.success(request, f"Thank you {full_name}, your order has been placed!")
        return redirect('request_list')
        
    return render(request, 'core/checkout.html')  