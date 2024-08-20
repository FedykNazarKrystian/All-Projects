from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    upload_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='songs/')

    def __str__(self):
        return f'{self.title} by {self.artist}'

class FavoriteSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"Favorite: {self.song.title}"

