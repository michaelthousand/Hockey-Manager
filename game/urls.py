from django.urls import path
from . import views

urlpatterns = [
    path('', views.live_game, name="live_game"),
]