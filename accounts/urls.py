from rest_framework_simplejwt import views as jwt_views
from django.urls import path
from . import views


urlpatterns = [
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path('accounts/', views.UserView.as_view()),
]