from django.db import models


# Create your models here.

class Genre(models.Model):
    name= models.CharField(max_length=255)

    def __str__(self):
        return self.name



class movie(models.Model):
    title=models.CharField(max_length=255)
    release_year=models.IntegerField()
    rate=models.FloatField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
