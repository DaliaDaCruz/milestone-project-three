from django.urls import path
from . import views

urlpatterns = [
    path('', views.request_list, name='request_list'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('request/new/', views.request_create, name='request_create'),
    path('request/<int:pk>/edit/', views.request_update, name='request_update'),
    path('request/<int:pk>/delete/', views.request_delete, name='request_delete'),
]