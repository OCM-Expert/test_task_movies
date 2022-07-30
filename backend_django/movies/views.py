from .serializers import FilmWorkSerializer, GenreSerializer, ActorSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FilmWork, Genre,  Person
from .selectors import *
from django.http import JsonResponse

class FilmWorksList(APIView):
    def get(self, request, format=None):
        genre = request.GET.get('genreToSelect')
        actor = request.GET.get('actorToSelect')
        if genre:
            genreID = Genre.objects.get(name=genre).id
            filmsByGenre = getFilmsByGenre(genreID)
            serializer = FilmWorkSerializer(filmsByGenre, many=True)
            return Response(serializer.data)
        if actor:
            actorExists = getPersonId(actor)
            if actorExists:
                actorID = Person.objects.get(full_name=actor).id
                filmsByActor = getFilmsByActor(actorID)
                serializer = FilmWorkSerializer(filmsByActor, many=True)
                return Response(serializer.data)
            else:
                filmsByActor = []
                serializer = FilmWorkSerializer(filmsByActor, many=True)
                return Response(serializer.data)
        else:
            products = FilmWork.objects.all()
            serializer = FilmWorkSerializer(products, many=True)
            return Response(serializer.data)


class GenresList(APIView):
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class ActorsList(APIView):
    def get(self, request, format=None):
        actors = Person.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)


def getPersonId(actor):
    try:
        return Person.objects.get(full_name=actor)
    except Person.DoesNotExist:
        return False


def RatingsPopularity(request):
    # do something with the your data
    data = getRatingsPopularity()
    # just return a JsonResponse
    return JsonResponse(data)


def GenresPopularity(request):
    data = getGenresPopularity()
    return JsonResponse(data)
