from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='user_login'),
    path('machines/', views.machine_list, name='machine_list'),
    path('machines/<slug:slug>/', views.machine_detail, name='machine_detail'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('cart/remove/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<str:order_number>/', views.order_success, name='order_success'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
]
