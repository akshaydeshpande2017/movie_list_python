from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.CharField(max_length=100)
    imdb_score = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    popularity = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)

    class Meta:
        unique_together = ('name', 'director')

    def __str__(self):
        return self.name
