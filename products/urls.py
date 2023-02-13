from django.urls import path
from . import views

urlpatterns = [
    path('load_json/', views.LoadGamesView.as_view(), name='load_games'),
    path('games/', views.GamesList.as_view(), name='games-list'),
]