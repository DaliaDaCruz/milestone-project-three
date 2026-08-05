def cart_counter(request):
    """Context processor to make cart item work"""
    cart = request.session.get('cart', {})
    total_count = 0

    if isinstance(cart, dict):
        for val in cart.values():
            # If cart stores item count directly as int or numeric string
            if isinstance(val, int):
                total_count += val
            elif isinstance(val, str) and val.isdigit():
                total_count += int(val)
            # If cart stores nested item dicts (e.g., {'quantity': 2, ...})
            elif isinstance(val, dict):
                qty = val.get('quantity', 0)
                if isinstance(qty, int):
                    total_count += qty
                elif isinstance(qty, str) and qty.isdigit():
                    total_count += int(qty)

    return {'cart_count': total_count}
