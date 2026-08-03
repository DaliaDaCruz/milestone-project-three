from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('booking/', views.booking, name='booking'),
    path('services/', views.services, name='services'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cart/add/<int:machine_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/success/<str:order_number>/', views.order_success, name='order_success'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]