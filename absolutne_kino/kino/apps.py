"""
Zadanie zaliczeniowe z języka Python  
Imię i nazwisko ucznia: Tomasz Gradowski
Data wykonania zadania: 19.05.2025
Treść zadania: Sprzedaż biletów w kinie  
Opis funkcjonalności aplikacji: Rejestruje konfigurację aplikacji Django odpowiedzialnej za obsługę kina.
"""


from django.apps import AppConfig

# Konfiguracja aplikacji Django o nazwie 'kino'
class KinoConfig(AppConfig):
    # Domyślne pole automatycznego klucza głównego dla modeli w tej aplikacji
    default_auto_field = 'django.db.models.BigAutoField'
    # Nazwa aplikacji
    name = 'kino'
