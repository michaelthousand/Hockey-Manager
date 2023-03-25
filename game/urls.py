from django.urls import path
from . import views

urlpatterns = [
    path('', views.live_game, name="live_game"),
    path('add_toi/', views.add_toi, name="add_toi"),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
]