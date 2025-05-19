"""
Zadanie zaliczeniowe z języka Python  
Imię i nazwisko ucznia: Tomasz Gradowski
Data wykonania zadania: 19.05.2025 
Treść zadania: Sprzedaż biletów w kinie  
Opis funkcjonalności aplikacji: Definiuje wygląd modeli Film i Seans w panelu administratora Django.
"""


from django.contrib import admin
from .models import Movie, Showing

# Rejestracja modelu Movie w panelu admina z dodatkowymi opcjami konfiguracji
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Pola wyświetlane na liście filmów w panelu admina
    list_display = ('title', 'price', 'release_date', 'movie_type')

# Rejestracja modelu Showing w panelu admina z dodatkowymi opcjami konfiguracji
@admin.register(Showing)
class ShowingAdmin(admin.ModelAdmin):
    # Pola wyświetlane na liście seansów w panelu admina
    list_display = ('movie', 'time')
