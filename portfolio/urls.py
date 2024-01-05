from django.contrib import admin
from django.urls import path, include
from api import urls as apiurls

from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(apiurls)),
    path('i18n/', set_language, name='set_language'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Wrap the urlpatterns with i18n_patterns to enable language-specific patterns

