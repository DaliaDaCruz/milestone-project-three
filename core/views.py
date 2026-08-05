from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Machine, Booking, Order, OrderItem


def index(request):
    """Render home page."""
    return render(request, 'core/index.html')


def catalog(request):
    """Render products/machines catalog."""
    machines = Machine.objects.all()
    return render(request, 'core/catalog.html', {'machines': machines})


def machine_detail(request, slug):
    """Render detail view for a specific machine."""
    machine = get_object_or_404(Machine, slug=slug)
    return render(request, 'core/machine_detail.html', {'machine': machine})


def services(request):
    """Render the services offered page."""
    return render(request, 'core/services.html')


def booking(request):
    """Render and handle the repair/service booking page."""
    selected_service = request.GET.get('service', '')

    if request.method == 'POST':
        service = request.POST.get('service')
        email = request.POST.get('email')
        name = request.POST.get('name')

        if service and email and name:
            Booking.objects.create(
                user=request.user if request.user.is_authenticated else None,
                name=name,
                email=email,
                service=service,
            )
            messages.success(
                request,
                "Your repair/service request has been submitted successfully!"
            )
            return redirect('dashboard')
        else:
            messages.error(request, "Please fill in all required fields.")

    context = {
        'selected_service': selected_service,
    }
    return render(request, 'core/booking.html', context)


@login_required
def dashboard(request):
    """Render user dashboard with user details, bookings, and activity."""
    user_bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')
    featured_machines = Machine.objects.all()[:3]

    context = {
        'user': request.user,
        'bookings': user_bookings,
        'orders': orders,
        'featured_machines': featured_machines,
    }
    return render(request, 'core/dashboard.html', context)

def cart(request):
    """Render the shopping basket/cart page."""
    cart_data = request.session.get('cart', {})
    cart_items = []
    subtotal = Decimal('0.00')

    if cart_data:
        machine_ids = [int(pk) for pk in cart_data.keys()]
        machines = Machine.objects.filter(id__in=machine_ids)

        for machine in machines:
            quantity = cart_data.get(str(machine.id)) or cart_data.get(machine.id) or 0
            if quantity > 0:
                item_total = machine.price * quantity
                subtotal += item_total

                cart_items.append({
                    'machine': machine,
                    'quantity': quantity,
                    'item_total': item_total,
                })

    shipping = Decimal('0.00')
    tax = subtotal * Decimal('0.20')
    total = subtotal + tax

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'shipping': shipping,
        'tax': tax,
        'total': total,
    }
    return render(request, 'core/cart.html', context)


def add_to_cart(request, machine_id):
    """Add a machine to the session-based shopping cart."""
    machine = get_object_or_404(Machine, id=machine_id)
    cart = request.session.get('cart', {})
    str_id = str(machine_id)

    cart[str_id] = cart.get(str_id, 0) + 1
    request.session['cart'] = cart

    messages.success(request, f"Added {machine.name} to your basket!")
    return redirect(request.META.get('HTTP_REFERER', 'catalog'))


def remove_from_cart(request, machine_id):
    """Remove a machine from the session-based shopping cart."""
    machine = get_object_or_404(Machine, id=machine_id)
    cart = request.session.get('cart', {})
    str_id = str(machine_id)

    if str_id in cart:
        del cart[str_id]
        request.session['cart'] = cart
        messages.info(request, f"Removed {machine.name} from your basket.")

    return redirect(request.META.get('HTTP_REFERER', 'catalog'))


def checkout(request):
    """Render checkout page with cart summary and handle order placement."""
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = Decimal('0.00')

    if cart:
        machine_ids = [int(pk) for pk in cart.keys()]
        machines = Machine.objects.filter(id__in=machine_ids)

        for machine in machines:
            quantity = cart.get(str(machine.id)) or cart.get(machine.id) or 0
            if quantity > 0:
                subtotal = machine.price * quantity
                total_price += subtotal

                cart_items.append({
                    'machine': machine,
                    'name': machine.name,
                    'price': machine.price,
                    'quantity': quantity,
                    'subtotal': subtotal,
                })

    if request.method == 'POST':
        if not cart_items:
            messages.error(request, "Your basket is empty!")
            return redirect('catalog')

        default_name = (
            request.user.get_full_name() or request.user.username
            if request.user.is_authenticated else ''
        )
        full_name = request.POST.get('full_name', default_name)
        email = request.POST.get(
            'email',
            request.user.email if request.user.is_authenticated else ''
        )
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        postcode = request.POST.get('postcode', '')

        import uuid
        order_number = str(uuid.uuid4()).split('-')[0].upper()

        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            postcode=postcode,
            total_price=total_price,
            order_number=order_number,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                machine=item['machine'],
                price=item['price'],
                quantity=item['quantity'],
            )

        request.session['cart'] = {}
        messages.success(
            request,
            f"Order #{order_number} placed successfully!"
        )
        return redirect('order_success', order_number=order_number)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'subtotal': total_price,
        'shipping': Decimal('0.00'),
        'tax': total_price * Decimal('0.20'),
        'total': total_price * Decimal('1.20'),
    }
    return render(request, 'core/checkout.html', context)


def order_success(request, order_number):
    """Render confirmation page after placing an order."""
    return render(
        request, 'core/order_success.html', {'order_number': order_number}
    )


def register(request):
    """Handle user registration."""
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f"Welcome to Coffee CPR, {user.username}!"
            )
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {'form': form})


def user_logout(request):
    """Log out current user."""
    logout(request)
    return redirect('index')


def custom_404(request, exception=None):
    """Custom 404 handler."""
    return render(request, 'core/404.html', status=404)


def custom_500(request):
    """Custom 500 handler."""
    return render(request, 'core/500.html', status=500)