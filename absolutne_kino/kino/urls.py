from django.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from absolutne_kino.kino import admin  # Import panelu admina z aplikacji kino\

urlpatterns = [
    # Ścieżka do panelu administracyjnego Django
    path('admin/', admin.site.urls),
    # Dołączenie wszystkich ścieżek z aplikacji 'kino'
    path('', include('kino.urls')),
]
# Import admina z aplikacji kino
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
