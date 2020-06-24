from django.shortcuts import render
from django.http import HttpResponse
from .models import movie
# Create your views here.

def index(requests):
    movies= movie.objects.all()
    return render(requests,'mymovies/index.html',{'movies': movies})

