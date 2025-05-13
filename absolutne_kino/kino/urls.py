from xml.etree.ElementInclude import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from absolutne_kino.kino import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kino.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)