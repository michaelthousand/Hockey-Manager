from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name="roster_home"),
    path('players/', views.PlayerList.as_view(), name='roster'),
    path('players/create', views.CreatePlayer.as_view(), name='createplayer'),
    path('players/<str:id>/update/', views.UpdatePlayer.as_view(), name='updateplayer'),
    path('players/<str:id>/delete/', views.DeletePlayer.as_view(), name='deleteplayer'),
    path('seasons/add', views.add_season, name='add_season'),
    path('lineup/', views.ViewLineup.as_view(), name="lineup"),
    path('notes/', views.ViewNotes.as_view(), name='roster_notes'),
    path('notes/add', views.CreateNote.as_view(), name="createnote"),
    
]