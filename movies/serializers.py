from rest_framework import serializers
from . models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Genre
        fields = ['name']


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['name', 'director', 'imdb_score', 'popularity', 'genre']
