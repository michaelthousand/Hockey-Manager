from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ViewNotes.as_view(), name='view_notes'),
    path('add', views.add_note, name='add_note'),
]