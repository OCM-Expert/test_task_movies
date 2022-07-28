from rest_framework import serializers
from .models import FilmWork

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
            'genres',
            'persons'
        )
