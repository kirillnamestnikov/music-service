from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('<slug:genre_slug>/', 
        views.song_list, 
        name='song_list_by_genre'),
    path('<int:id>/<slug:slug>/', views.song_detail,
        name='song_detail'),
]