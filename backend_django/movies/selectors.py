import uuid
from .models import PersonFilmWork, FilmWork, GenreFilmWork,Genre


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
