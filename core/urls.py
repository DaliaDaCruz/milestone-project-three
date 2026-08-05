# Imports MUST be at the very top of the file (Fixes E402)
from django.urls import path
from . import views

urlpatterns = [
    # ... existing paths above ...
    path(
        'cart/remove/<int:machine_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
    path('checkout/', views.checkout, name='checkout'),
    path(
        'order-success/<str:order_number>/',
        views.order_success,
        name='order_success'
    ),

    # AUTH PATHS (Fixes E131 alignment)
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
]
