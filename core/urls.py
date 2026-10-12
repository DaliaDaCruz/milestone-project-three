from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('requests/', views.request_list, name='request_list'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('request/new/', views.request_create, name='request_create'),
    path('request/<int:pk>/edit/', views.request_update, name='request_update'),
    path('request/<int:pk>/delete/', views.request_delete, name='request_delete'),
    path('basket/add/<int:product_id>/', views.add_to_basket, name='add_to_basket'),
    path('basket/update/<int:product_id>/', views.update_basket, name='update_basket'),
    path('basket/remove/<int:product_id>/', views.remove_from_basket, name='remove_from_basket'),
]