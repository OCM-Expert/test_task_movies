from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import FilmWork
from .models import Person
from .models import PersonFilmWork
from django.core import serializers
from .services import MoviesService
import  uuid

from django.db import connection

movies_service = MoviesService()

def index(request):
    filter = request.GET["filter"]
    text = request.GET["text"]
    print(filter,text)

    if(text==""):
        films_list = list(FilmWork.objects.all().values())
        return JsonResponse(films_list, safe=False)
    elif(filter=='actor'):
        films_by_selected_actor = movies_service.get_filtered_films_by_actor(text)
        return JsonResponse(films_by_selected_actor, safe=False)
    else:
        films_by_selected_genre = movies_service.get_filtered_films_by_genre(text)
        return JsonResponse(films_by_selected_genre, safe=False)

def get_diagram_data(request):
    rating_diagram_data = movies_service.get_ratings()
    genres_by_popularity_data = movies_service.get_genre_popularity()

    diagram_data = {
        'rating_diagram_data':rating_diagram_data,
        'genres_by_popularity_data': genres_by_popularity_data
    }

    return JsonResponse(diagram_data, safe=False)

