from django.db import models

class Film(models.Model):

    title = models.CharField(max_length=100, null=False, blank=False, default="")
    year = models.IntegerField(null=False, blank=False)
    director = models.CharField(max_length=100, null=False, blank=False, default="")
    rating = models.FloatField(null=False, blank=False)
    genre = models.CharField(max_length=100, null=False, blank=False, default="")
    runtime = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, default="")
    photo = models.ImageField(blank=True, upload_to="photos/")
    is_saved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

