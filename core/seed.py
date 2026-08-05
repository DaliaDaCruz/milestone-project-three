from core.models import Product

products_data = [
    {
        'name': 'Espresso Roast Blend',
        'category': 'Beans',
        'price': 14.99,
        'description': (
            'Rich, dark roast with notes of dark chocolate, caramel, '
            'and toasted almond.'
        ),
        'badge': 'Best Seller',
        'image_url': (
            'https://images.unsplash.com/photo-1559056199-641a0ac8b55e'
            '?w=500&q=80'
        ),
    },
    {
        'name': 'Ethiopian Yirgacheffe',
        'category': 'Beans',
        'price': 16.50,
        'description': (
            'Light roast featuring floral aroma, bergamot tea notes, '
            'and bright citrus acidity.'
        ),
        'badge': 'Single Origin',
        'image_url': (
            'https://images.unsplash.com/photo-1587734195503-904fca47e0e9'
            '?w=500&q=80'
        ),
    },
    {
        'name': 'Decaf Swiss Water Process',
        'category': 'Beans',
        'price': 15.00,
        'description': (
            'Smooth medium roast with full flavor, subtle hazelnut, '
            'and zero jitters.'
        ),
        'badge': 'Decaf',
        'image_url': (
            'https://images.unsplash.com/photo-1611854779393-1b2da9d400fe'
            '?w=500&q=80'
        ),
    },
    {
        'name': 'Stainless Steel French Press',
        'category': 'Equipment',
        'price': 34.99,
        'description': (
            'Double-wall insulated 34oz press that keeps your brew hot '
            'for hours.'
        ),
        'badge': 'Gear',
        'image_url': (
            'https://images.unsplash.com/photo-1544787219-7f47ccb76574'
            '?w=500&q=80'
        ),
    },
    {
        'name': 'Precision Coffee Scale',
        'category': 'Equipment',
        'price': 24.95,
        'description': (
            'Digital scale with built-in timer for accurate pour-over '
            'brewing ratio.'
        ),
        'badge': 'Gear',
        'image_url': (
            'https://images.unsplash.com/photo-1517256064527-09c73fc73e38'
            '?w=500&q=80'
        ),
    },
    {
        'name': 'Coffee CPR Travel Mug',
        'category': 'Merchandise',
        'price': 19.99,
        'description': (
            '16oz vacuum-insulated stainless steel tumbler with '
            'leak-proof lid.'
        ),
        'badge': 'New',
        'image_url': (
            'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd'
            '?w=500&q=80'
        ),
    },
]

for p in products_data:
    Product.objects.get_or_create(name=p['name'], defaults=p)

print("Products added successfully!")
