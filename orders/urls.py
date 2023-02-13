from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderView.as_view(), name='games-list'),
    path('orders/<uuid:pk>/', views.OrderDetailView.as_view(), name='games-list'),
]