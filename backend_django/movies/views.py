from .serializers import FilmWorkSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FilmWork

class FilmWorksList(APIView):
    def get(self, request, format=None):
        products = FilmWork.objects.all()[0:4]
        serializer = FilmWorkSerializer(products, many=True)
        return Response(serializer.data)


# def index(request):
#     movies = getAllMovies()
#     getMoviesByActor('Harrison Ford')
#     return render(request, 'movies/index.html', {
#         'movies': movies
#     })
#
# def getAllMovies():
#     return FilmWork.objects.all()
#
# def getMoviesByActor(actorName):
#     actorId = Person.objects.get(full_name=actorName).id
#     actorId = uuid.UUID(str(actorId))
#     matches = PersonFilmWork.objects.filter(person_id=actorId)
#     return matches