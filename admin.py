from django.contrib import admin
from .models import Genre,movie

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display=('id','name')


class Movieadmin(admin.ModelAdmin):
    list_display=('id','title','release_year','rate','genre_id')



admin.site.register(Genre,GenreAdmin) ,
admin.site.register(movie,Movieadmin)

