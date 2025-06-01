from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_songs, name='list_songs'),
    path('delete/<int:song_id>/', views.delete_song, name='delete_song'),
    path('download/<int:song_id>/', views.download_song, name='download_song'),
]
