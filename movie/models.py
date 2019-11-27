from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    movieid = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=55)
    requested = models.IntegerField(default=0)
    year = models.CharField(max_length=4)
    length = models.CharField(max_length=10)
    genres = models.CharField(max_length=100)
    rate = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    poster = models.URLField(default='')
    plot = models.CharField(max_length=500)
    trailer = models.URLField(default='', max_length=500)
    timestamp  = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @staticmethod
    def get_name():
        return 'movie'

class Frame(models.Model):
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    frame = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    movieid = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    timestamp  = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment[:30]

class ActorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

class Actor(models.Model):
    actorid = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=30)
    photo = models.URLField()

    objects = ActorManager()

    def __str__(self):
        return self.name

    @staticmethod
    def get_name():
        return 'actor'


class Act(models.Model):
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)
    actorid = models.ForeignKey('Actor', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.actorid.actorid + '|' + self.movieid.movieid


class Seen(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.username + '|' + self.movieid.movieid


class Expect(models.Model):
    username = models.CharField(max_length=150)
    movieid = models.ForeignKey('Movie', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.username + '|' + self.movieid.movieid

