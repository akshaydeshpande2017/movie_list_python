from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MovieManager(models.Manager):
    def filter_movies(self, filters):
        query = models.Q()
        for key, value in filters.items():
            if not value:
                continue
            field = Movie._meta.get_field(key)
            field_type = field.get_internal_type()
            if field_type == "CharField":
                query.add(models.Q(**{key + '__icontains': value}), models.Q.AND)
            elif field_type == "FloatField":
                query.add(models.Q(**{key + '__gte': value}), models.Q.AND)
            elif field_type == "ManyToManyField":
                query.add(models.Q(**{key + '__name__in': value}), models.Q.AND)
        if query:
            return self.filter(query)


class Movie(models.Model):
    director = models.CharField(max_length=100)
    imdb_score = models.FloatField(default=0)
    name = models.CharField(max_length=100)
    popularity = models.FloatField(default=0)
    genre = models.ManyToManyField(Genre)

    objects = MovieManager()

    class Meta:
        unique_together = ('name', 'director')

    def __str__(self):
        return self.name
