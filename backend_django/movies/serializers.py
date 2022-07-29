from rest_framework import serializers
from .models import FilmWork, Genre

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