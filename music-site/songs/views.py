# songs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from .models import Song
from .forms import SongForm
from mutagen import File as AudioFile
import os
from django.conf import settings

def list_songs(request):
    songs = Song.objects.order_by('position')

    if request.method == 'POST' and request.user.is_staff:
        uploaded_file = request.FILES.get('song_file')
        if uploaded_file:
            song = Song()
            song.file = uploaded_file
            song.title = uploaded_file.name
            song.size = f"{round(song.file.size / (1024 * 1024), 2)} MB"

            audio = AudioFile(song.file)
            if audio and audio.info:
                duration_seconds = int(audio.info.length)
                minutes = duration_seconds // 60
                seconds = duration_seconds % 60
                song.duration = f"{minutes}:{str(seconds).zfill(2)}"
            else:
                song.duration = "Unknown"

            song.position = Song.objects.count()
            song.save()
            return redirect('list_songs')

    for song in songs:
        song.full_url = request.build_absolute_uri(song.file.url)

    return render(request, 'songs/song_list.html', {
        'songs': songs,
    })


@login_required
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.user.is_staff:
        song.file.delete()
        song.delete()
    return redirect('list_songs')



def download_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song.download_count += 1
    song.save()
    response = FileResponse(song.file.open('rb'), as_attachment=True, filename=song.file.name)
    return response
