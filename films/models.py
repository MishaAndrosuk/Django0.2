from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    rating = models.FloatField()
    genre = models.CharField(max_length=100)
    runtime = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title
