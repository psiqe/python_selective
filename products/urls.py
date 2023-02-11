from django.urls import path
from .insertJsonProducts import load_games
# from .views import GamesList
from . import views

urlpatterns = [
    path('load_json/', load_games, name='load_games'),
    path('games/', views.GamesList.as_view(), name='games-list'),
]