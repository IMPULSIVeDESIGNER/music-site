from django.db import models
from django.utils import timezone

class Song(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='songs/')
    duration = models.CharField(max_length=10, blank=True)
    size = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    position = models.PositiveIntegerField(default=0)
    download_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# songs/forms.py
from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['file']
