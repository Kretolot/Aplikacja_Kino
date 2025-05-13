from django.contrib import admin
from .models import Movie, Showing

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'release_date', 'movie_type')

@admin.register(Showing)
class ShowingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'time')