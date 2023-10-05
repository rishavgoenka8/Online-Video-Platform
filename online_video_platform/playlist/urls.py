from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.Index.as_view(), name='all_playlists'),
    path('create_playlist/', views.CreatePlaylist.as_view(), name='create_playlist'),
    path('<int:pk>/', views.PlaylistVideos.as_view(), name='playlist_videos'),
    path('add_to_playlist/<int:pk1>/<int:pk2>', views.add_to_playlist, name='add_to_playlist'),
    path('delete_from_playlist/<int:pk1>/<int:pk2>', views.delete_from_playlist, name='delete_from_playlist'),
    path('delete_playlist/<int:pk>/', views.DeletePlaylist.as_view(), name='delete_playlist'),
]