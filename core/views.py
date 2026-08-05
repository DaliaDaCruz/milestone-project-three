import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Machine, Order 

# AUTHENTICATION VIEWS

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('index')

# PUBLIC PAGES & CATALOG VIEWS


def index(request):
    return render(request, 'core/index.html')


def catalog(request):
    machines = Machine.objects.all()
    return render(request, 'core/catalog.html', {'machines': machines})


def machine_detail(request, slug):
    machine = get_object_or_404(Machine, slug=slug)
    return render(request, 'core/machine_detail.html', {'machine': machine})


def services(request):
    return render(request, 'core/services.html')


@login_required
def booking(request):
    return render(request, 'core/booking.html')


@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'core/dashboard.html', {'orders': orders})

# CART & CHECKOUT VIEWS 


def cart(request):
    cart_session = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for machine_id, quantity in cart_session.items():
        try:
            machine = Machine.objects.get(id=machine_id)
            subtotal = machine.price * quantity
            total_price += subtotal
            cart_items.append({
                'machine': machine,
                'quantity': quantity,
                'subtotal': subtotal,
            })
        except Machine.DoesNotExist:
            continue

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'core/cart.html', context)


@require_POST
def add_to_cart(request, machine_id):
    machine = get_object_or_404(Machine, id=machine_id)
    cart_session = request.session.get('cart', {})
    str_id = str(machine_id)

    quantity = int(request.POST.get('quantity', 1))

    if str_id in cart_session:
        cart_session[str_id] += quantity
    else:
        cart_session[str_id] = quantity

    request.session['cart'] = cart_session
    messages.success(request, f'Added {machine.name} to your cart.')
    return redirect('catalog')


@require_POST
def remove_from_cart(request, machine_id):
    cart_session = request.session.get('cart', {})
    str_id = str(machine_id)

    if str_id in cart_session:
        del cart_session[str_id]
        request.session['cart'] = cart_session
        messages.success(request, 'Item removed from cart.')

    return redirect('catalog')


@login_required
def checkout(request):
    cart_session = request.session.get('cart', {})
    if not cart_session:
        messages.warning(request, 'Your cart is empty.')
        return redirect('catalog')

    if request.method == 'POST':
        order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"

        # Clear cart upon success
        request.session['cart'] = {}
        
        return redirect('order_success', order_number=order_number)
    return render(request, 'core/checkout.html')

def order_success(request, order_number):


    return render(request, 'core/order_success.html', {'order_number': order_number})

def checkout_success(request):
    return render(request, 'core/checkout_success.html')

def checkout_cancel(request):
    return render(request, 'core/checkout_cancel.html')

