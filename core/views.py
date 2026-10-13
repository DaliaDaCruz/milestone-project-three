from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Product, ServiceRequest  

# Static catalog fallback matching your index.html static product IDs
PRODUCTS_DATA = {
    1: {"id": 1, "name": "Galileo", "price": Decimal('3349.99'), "image": "assets/images/galileo.png"},
    2: {"id": 2, "name": "Monza", "price": Decimal('3289.99'), "image": "assets/images/monza.png"},
    3: {"id": 3, "name": "Lira", "price": Decimal('2342.50'), "image": "assets/images/lira.png"},
    4: {"id": 4, "name": "Classic2gruppi", "price": Decimal('3232.50'), "image": "assets/images/classic2gruppi.png"},
    5: {"id": 5, "name": "Classica", "price": Decimal('3414.99'), "image": "assets/images/classica.png"},
    6: {"id": 6, "name": "Fiorenzato F64", "price": Decimal('1598.99'), "image": "assets/images/fiorenzato.png"},
    7: {"id": 7, "name": "58mm Bottomless Portafilter", "price": Decimal('45.00'), "image": "assets/images/portafilter.jpg"},
}

# --- Main Page Views ---

def index_view(request):
    """Homepage view."""
    products = Product.objects.all()
    return render(request, 'core/index.html', {'products': products})


def request_list(request):
    """Workshop requests / product catalog view."""
    # Fetch all submitted service requests from the database
    requests_list = ServiceRequest.objects.all().order_by('-created_at')
    
    # Also fetch products if you display products on this page
    products = Product.objects.all()

    context = {
        'requests': requests_list,
        'products': products,
    }
    return render(request, 'core/request_list.html', context)

def checkout_view(request):
    """Unified basket and checkout summary view with DB lookup and dictionary fallback."""
    basket = request.session.get('basket', {})
    basket_items = []
    subtotal = Decimal('0.00')

    for product_id_str, quantity in basket.items():
        try:
            p_id = int(product_id_str)
            
            # 1. Check Database first
            try:
                product_obj = Product.objects.get(id=p_id)
                name = product_obj.name
                price = product_obj.price
                image_url = product_obj.image.url if product_obj.image else None
            except Product.DoesNotExist:
                # 2. Fall back to static dictionary if item isn't in database
                if p_id in PRODUCTS_DATA:
                    fallback = PRODUCTS_DATA[p_id]
                    name = fallback['name']
                    price = fallback['price']
                    image_url = fallback['image']
                else:
                    continue

            total_price = price * quantity
            subtotal += total_price
            
            basket_items.append({
                'product_id': p_id,
                'name': name,
                'price': price,
                'image_url': image_url,
                'quantity': quantity,
                'total_price': total_price,
            })
        except ValueError:
            continue

    shipping = Decimal('15.00') if subtotal > Decimal('0.00') else Decimal('0.00')
    grand_total = subtotal + shipping

    context = {
        'basket_items': basket_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'core/checkout.html', context)


# --- Request CRUD Views ---

def request_create(request):
    """Create a new service/equipment request."""
    if request.method == "POST":
        customer_name = request.POST.get('name')
        machine_model = request.POST.get('machine_model')
        issue_description = request.POST.get('description')

        req_obj = ServiceRequest()

        # Handle customer name attribute
        if hasattr(req_obj, 'customer_name'):
            req_obj.customer_name = customer_name
        elif hasattr(req_obj, 'name'):
            req_obj.name = customer_name

        req_obj.machine_model = machine_model

        # Handle description attribute
        if hasattr(req_obj, 'issue_description'):
            req_obj.issue_description = issue_description
        elif hasattr(req_obj, 'description'):
            req_obj.description = issue_description

        # Set default status if status exists on model
        if hasattr(req_obj, 'status') and not req_obj.status:
            req_obj.status = 'Pending'

        try:
            req_obj.save()
            print(f"SUCCESS: Saved Service Request #{req_obj.pk} to database!")
        except Exception as e:
            print("=" * 40)
            print(f"DATABASE SAVE ERROR: {e}")
            print("=" * 40)

        # Console feedback to verify submissions live
        print("=" * 40)
        print(f"NEW SERVICE REQUEST: {customer_name} | Machine: {machine_model}")
        print(f"Details: {issue_description}")
        print("=" * 40)

        messages.success(request, f"Thank you {customer_name}! Your service request for {machine_model} has been received.")
        return redirect('index')

    return render(request, 'core/request_form.html')


def request_update(request, pk):
    """Update an existing request."""
    return render(request, 'core/request_form.html')


def request_delete(request, pk):
    """Delete a request."""
    return redirect('request_list')


# --- Basket Action Views ---

def add_to_basket(request, product_id):
    """Add or increment product quantity in session basket."""
    basket = request.session.get('basket', {})
    product_id_str = str(product_id)

    if request.method == "POST":
        try:
            quantity = int(request.POST.get('quantity', 1))
        except ValueError:
            quantity = 1
    else:
        quantity = 1

    basket[product_id_str] = basket.get(product_id_str, 0) + quantity

    request.session['basket'] = basket
    request.session.modified = True

    return redirect('checkout')


def update_basket(request, product_id):
    """Update item quantity directly from the checkout page."""
    if request.method == "POST":
        basket = request.session.get('basket', {})
        product_id_str = str(product_id)
        
        try:
            quantity = int(request.POST.get('quantity', 1))
            if quantity > 0:
                basket[product_id_str] = quantity
            else:
                basket.pop(product_id_str, None)
        except ValueError:
            pass

        request.session['basket'] = basket
        request.session.modified = True
        
    return redirect('checkout')


def remove_from_basket(request, product_id):
    """Remove item completely from the basket."""
    if request.method == "POST":
        basket = request.session.get('basket', {})
        product_id_str = str(product_id)

        if product_id_str in basket:
            del basket[product_id_str]
            request.session['basket'] = basket
            request.session.modified = True

    return redirect('checkout')