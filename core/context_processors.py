def cart_counter(request):
    """Return the total quantity of items in the cart across all views."""
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return {'cart_count': total_items}
