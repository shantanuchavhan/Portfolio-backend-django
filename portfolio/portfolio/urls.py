from django.contrib import admin
from django.urls import path, include
from api import urls as apiurls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apiurls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


