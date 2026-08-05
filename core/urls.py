from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('machine/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # --- CART & CHECKOUT PATHS ---
    path('cart/', views.cart, name='cart'),  # <-- ADD THIS LINE
    path('cart/add/<int:machine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<str:order_number>/', views.order_success, name='order_success'),

        # --- AUTH PATHS ---
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
]
