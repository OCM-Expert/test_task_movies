from django.urls import path
from movies import views

urlpatterns = [
    path('film-works-list', views.FilmWorksList.as_view(), name='index'),
    path('genres-list', views.GenresList.as_view(), name='index')
]
