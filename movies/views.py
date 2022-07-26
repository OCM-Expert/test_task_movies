from django.shortcuts import render
from .models import FilmWork

def index(request):
    movies = FilmWork.objects.all()
    return render(request, 'movies/index.html', {
        'movies': movies
    })