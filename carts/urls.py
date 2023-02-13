from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='carts'),
    path('cart/<uuid:pk>/', views.CartDetailView.as_view(), name='cart'),
]