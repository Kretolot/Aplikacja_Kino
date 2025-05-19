"""
Zadanie zaliczeniowe z języka Python  
Imię i nazwisko ucznia: Tomasz Gradowski
Data wykonania zadania: 19.05.2025
Treść zadania: Sprzedaż biletów w kinie  
Opis funkcjonalności aplikacji: Konfiguruje główne ścieżki URL projektu Django, w tym panel administratora i przekierowanie do aplikacji 'kino'.
"""


from django.contrib import admin
from django.urls import path, include   
from kino import views  # Import widoków z aplikacji "kino"

# Używane w szablonach przy korzystaniu z przestrzeni nazw
app_name = 'kino'

# Lista obsługiwanych ścieżek URL
urlpatterns = [
    path('admin/', admin.site.urls),  # Panel administracyjny Django

    path('', views.home, name='home'),  # Strona główna (lista filmów)

    # Ścieżka do przekierowania po zakupie biletu (np. do PDF lub biletu)
    path('movie/<int:movie_id>/ticket/', views.ticket_redirect, name='ticket_redirect'),

    # Szczegóły filmu i wybór miejsc
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),

    # Strona "Wkrótce w kinie"
    path('coming-soon/', views.coming_soon, name='coming_soon'),

    # API zwracające zajęte miejsca dla danego seansu (np. używane w JS)
    path('get-taken-seats/<int:showing_id>/', views.get_taken_seats, name='get_taken_seats'),
]

# Obsługa plików multimedialnych w trybie deweloperskim (np. zdjęcia filmów)
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
