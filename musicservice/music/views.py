from django.shortcuts import render, get_object_or_404
from .models import Genre, Song

def song_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    songs = Song.objects.all()
    if genre_slug:
        genre = get_object_or_404(Genre,
                                  slug=genre_slug)
        songs = songs.filter(genre=genre)
    return render(request,
                  'music/song/list.html',
                  {'genre': genre,
                   'genres': genres,
                   'songs': songs
                   })


def song_detail(request, id, slug):
    song = get_object_or_404(
        Song,
        id=id,
        slug=slug
    )
    return render(request,
                  'music/song/detail.html',
                  {'song': song})