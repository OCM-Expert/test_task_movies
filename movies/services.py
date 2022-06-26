from .models import PersonFilmWork, FilmWork, GenreFilmWork,Genre

class MoviesService:
    films_list = list(FilmWork.objects.all().values())
    all_genres = list(Genre.objects.all().values())
    all_genre_film_work = list(GenreFilmWork.objects.all().values())
    def get_filtered_films_by_actor(self,actor_name):
        films = []
        film_works = list(PersonFilmWork.objects.filter(person_id__full_name__contains=actor_name).values())

        for film in self.films_list:
            for film_work in film_works:
                if(film["id"] == film_work["film_work_id_id"]):
                    films.append(film)
        return films

    def get_filtered_films_by_genre(self, genre):
        films = []
        films_in_selected_genre = list(GenreFilmWork.objects.filter(genre_id__name__contains=genre).values())

        for film in self.films_list:
            for selected_films in films_in_selected_genre:
                if(film["id"]==selected_films["film_work_id_id"]):
                    films.append(film)
        return films

    def get_ratings(self):
        result = {}
        for film in self.films_list:
            rating = film["rating"]
            if(rating in result):
                result[rating] += 1
            else:
                result[rating] = 1
        return result

    def get_genre_popularity(self):
        result={}
        for genre in self.all_genres:
            genre_name = genre["name"]
            for genre_film_work in self.all_genre_film_work:
                if(genre_film_work['genre_id_id']==genre['id']):
                    if (genre_name in result):
                        result[genre_name] += 1
                    else:
                        result[genre_name] = 1

        return result


