from .serializers import FilmWorkSerializer, GenreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FilmWork, Genre, GenreFilmWork
from .selectors import *

class FilmWorksList(APIView):
    def get(self, request, format=None):
        genre = request.GET.get('genreToSelect')

        print(genre)
        if genre:
            genreID = Genre.objects.get(name=genre).id
            print(genreID)
            filmsByGenre = getFilmsByGenre(genreID)
            serializer = FilmWorkSerializer(filmsByGenre, many=True)
            return Response(serializer.data)
        else:
            products = FilmWork.objects.all()
            serializer = FilmWorkSerializer(products, many=True)
            return Response(serializer.data)
        # if genres:
        #     genre = genres[0]
        #     films = []
        #     films_list = list(FilmWork.objects.all().values())
        #     films_in_selected_genre = list(GenreFilmWork.objects.filter(genre_id__name__contains=genre).values())
        #
        #     for film in films_list:
        #         for selected_films in films_in_selected_genre:
        #             if film["id"] == selected_films["film_work_id_id"]:
        #                 films.append(film)
        #     serializer = FilmWorkSerializer(films, many=True)
        #     return Response(serializer.data)
        # else:
        #     products = FilmWork.objects.all()[0:10]
        #     serializer = FilmWorkSerializer(products, many=True)
        #     return Response(serializer.data)


class GenresList(APIView):
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
