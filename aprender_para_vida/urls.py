from django.contrib import admin
from django.urls import path, include
from src.views import index
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
