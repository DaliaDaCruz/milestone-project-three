from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('services/', views.services, name='services'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:machine_id>/', views.add_to_cart, name='add_to_cart'), 
    path('cart/remove/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('booking/', views.booking, name='booking'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
    path('checkout/cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('machine/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('logout/', views.user_logout, name='logout'),  
    
]
