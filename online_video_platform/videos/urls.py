from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('upload/', views.UploadVideo.as_view(), name='upload_video'),
    path('<int:pk>/', views.DetailVideo.as_view(), name='video_detail'),
    path('<int:pk>/delete/', views.DeleteVideo.as_view(), name='delete_video'),
    path('<int:pk>/like/', views.add_like, name='add_like'),
    path('search/', views.SearchVideo.as_view(), name='search_video'),
    path('<int:pk>/save/', views.save_video, name='save_video'),
    path('saved/', views.SavedVideo.as_view(), name='saved_video'),
]