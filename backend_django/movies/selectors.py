import uuid
from .models import PersonFilmWork, FilmWork, GenreFilmWork,Genre

class GenreIDPopularity:
    genreID = ''
    popularity = 0

def getFilmsByGenre(genre):
    allGenreFilmWork = list(GenreFilmWork.objects.all().values())
    allFilms = list(FilmWork.objects.all().values())
    filmsIDs = []
    films = []
    genreUUID = uuid.UUID(str(genre))
    for genreFilm in allGenreFilmWork:
        if genreFilm['genre_id_id'] == genreUUID:
            filmsIDs.append(genreFilm['film_work_id_id'])
    for film in allFilms:
        if film['id'] in filmsIDs:
            films.append(film)
    return films


def getFilmsByActor(actor):
    allFilms = list(FilmWork.objects.all().values())
    films = []
    filmIDs = []
    actorUUID = uuid.UUID(str(actor))
    personFilmWorks = []
    allpersonFilmWorks = list(PersonFilmWork.objects.filter(role='actor').values())
    for personFilmWork in allpersonFilmWorks:
        if personFilmWork['person_id_id'] == actorUUID:
            filmIDs.append(personFilmWork['film_work_id_id'])
    for film in allFilms:
        if film['id'] in filmIDs:
            films.append(film)
    return films


def getRatingsPopularity():
    result = {}
    allFilms = list(FilmWork.objects.exclude(rating=None).values())
    for film in allFilms:
        rating = film["rating"]
        if rating in result:
            result[rating] += 1
        else:
            result[rating] = 1
    return result

def getGenresPopularity():
    result = {}
    allGenres = list(Genre.objects.all().values())
    allGenresIDs = []
    genreIDPopularity = {}
    for genre in allGenres:
        genreID = genre['id']
        allGenresIDs.append(genreID)
        genreIDPopularity[genreID] = 0
    allGenresFilmWorks = list(GenreFilmWork.objects.all().values())
    for genreFilmWork in allGenresFilmWorks:
        genreID = genreFilmWork['genre_id_id']
        filmWorkID = genreFilmWork['film_work_id_id']
        genreIDPopularity[genreID] += 1

    genreUUID = uuid.UUID(str('56b541ab-4d66-4021-8708-397762bff2d4'))
    for genre in allGenres:
        result[genre['name']] = genreIDPopularity[genre['id']]
    return result
