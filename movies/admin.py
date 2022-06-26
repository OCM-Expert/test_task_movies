from django.contrib import admin
from .models import Genre
from .models import Person
from .models import GenreFilmWork
from .models import PersonFilmWork
from .models import FilmWork

# Register your models here.
admin.site.register(Genre)
admin.site.register(Person)
admin.site.register(GenreFilmWork)
admin.site.register(FilmWork)
admin.site.register(PersonFilmWork)
