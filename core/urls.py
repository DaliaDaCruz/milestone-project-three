from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cart/remove/<int:machine_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/<str:order_number>/', views.order_success, name='order_success'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='user_logout'),
]
