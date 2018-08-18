from django.db import models
import datetime
import django
# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=200)
    youtube_link = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class Playlist(models.Model):
    playlist_title = models.CharField(max_length=200)
    playlist_link = models.CharField(max_length=200)
    song = models.ManyToManyField(Song)
    def __str__(self):
        return self.playlist_title

class View(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    # view_date = models.DateField(default=datetime.date.today())
    view_date = models.DateField(default=django.utils.timezone.now)
    # def __str__(self):
    #     return self.view_count