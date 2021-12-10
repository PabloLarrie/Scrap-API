from django.db import models

class Pelicula(models.Model):
    id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=150, unique=True)
    Rating = models.FloatField(default=0)
    Year = models.IntegerField(default=0)
    
