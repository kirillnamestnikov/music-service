from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
                models.Index(fields=['name']),
        ]
        verbose_name = 'genre'
        verbose_name_plural = 'genres'

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200,
                            unique=True)
    thumbnail = models.ImageField(upload_to='artists/%Y/%m/%d',
                                  blank=True)
    bio = models.TextField(blank=False)

    class Meta:
        ordering = ['name']
        indexes = [
                models.Index(fields=['id', 'slug']),
                models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name


class Song(models.Model):
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=False)
    thumbnail = models.ImageField(upload_to='song_thumbnails/%Y/%m/%d',
                                  blank=False)
    song = models.FileField(upload_to='songs/%Y/%m/%d')
    artists = models.ManyToManyField(Artist, related_name='songs')
    size = models.IntegerField(default=0)
    playtime = models.CharField(max_length=15, default="0:00")
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
                models.Index(fields=['id', 'slug']),
                models.Index(fields=['name']),
                models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name
