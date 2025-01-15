from django.urls import path
from . import views

urlpatterns = [
    path('', views.snake, name='snake_game'),
    path('highscores/', views.highscores, name='highscores'),
    path('', views.snake, name='snake_game'),
]
