from django.urls import path
from . import views

urlpatterns = [
    path('carts/', views.CartView.as_view(), name='carts'),
    path('carts/<uuid:pk>/', views.CartDetailView.as_view(), name='cart'),
]