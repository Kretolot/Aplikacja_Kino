from django.apps import AppConfig

# Konfiguracja aplikacji Django o nazwie 'kino'
class KinoConfig(AppConfig):
    # Domyślne pole automatycznego klucza głównego dla modeli w tej aplikacji
    default_auto_field = 'django.db.models.BigAutoField'
    # Nazwa aplikacji
    name = 'kino'
