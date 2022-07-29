import uuid
from .models import PersonFilmWork, FilmWork, GenreFilmWork,Genre


def getFilmsByGenre(genre):
    allGenreFilmWork = list(GenreFilmWork.objects.all().values())
    allFilms = list(FilmWork.objects.all().values())
    filmsIDs = []
    films = []
    genreUUID = uuid.UUID(str(genre))
    print(type(genreUUID), genreUUID)
    for genreFilm in allGenreFilmWork:
        if genreFilm['genre_id_id'] == genreUUID:
            filmsIDs.append(genreFilm['film_work_id_id'])
    print(filmsIDs)
    for film in allFilms:
        if film['id'] in filmsIDs:
            films.append(film)
            print(film)
    return films

