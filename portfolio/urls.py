from django.contrib import admin
from django.urls import path, include
from api import urls as apiurls

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
]

# Wrap the urlpatterns with i18n_patterns to enable language-specific patterns
urlpatterns += i18n_patterns(
    path('', include(apiurls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
