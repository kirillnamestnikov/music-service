from django.contrib import admin
from .models import Genre, Artist, Song

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'size',
                    'playtime', 'featured', 'created',
                    'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
