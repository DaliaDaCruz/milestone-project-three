def cart_counter(request):
    """Context processor to make cart item count available to all templates safely."""
    cart = request.session.get('cart', {})
    total_count = 0
    
    if isinstance(cart, dict):
        for val in cart.values():
            if isinstance(val, int):
                total_count += val
            elif isinstance(val, str) and val.isdigit():
                total_count += int(val)
                
    return {'cart_count': total_count}