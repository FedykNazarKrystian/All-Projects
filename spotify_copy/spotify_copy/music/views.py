from django.shortcuts import render, get_object_or_404, redirect
from .models import Song, FavoriteSong
from .forms import SongForm

def songs(request):
    all_songs = Song.objects.all()
    return render(request, 'music/songs.html', {'all_songs': all_songs})

def listening(request, id):
    song = get_object_or_404(Song, id=id)
    return render(request, 'music/listening.html', {'song': song})

def upload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('songs')
    else:
        form = SongForm()
    return render(request, 'music/upload.html', {'form': form})

def favorite(request):
    favorite_songs = FavoriteSong.objects.all()
    return render(request, 'music/favorite.html', {'favorite_songs': favorite_songs})

def add_to_favorite(request, id):
    song = get_object_or_404(Song, id=id)
    FavoriteSong.objects.create(song=song)
    return redirect('favorite')


def remove_from_favorites(request, id):
    song = get_object_or_404(Song, id=id)
    favorites = FavoriteSong.objects.filter(song=song).first()
    if favorite:
        favorites.delete()
    return redirect('favorite')
