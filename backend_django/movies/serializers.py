from rest_framework import serializers
from .models import FilmWork, Genre, Person


class FilmWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmWork
        fields = (
            'title',
            'description',
            'creation_date',
            'certificate',
            'file_path',
            'rating',
            'type',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'name',
        )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'full_name',
        )
