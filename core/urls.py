from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-to-cart/<int:machine_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<str:order_number>/', views.order_success, name='order_success'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]