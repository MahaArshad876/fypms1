from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from FYPS import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app_project.urls")),
]+static(settings.STATIC_URL, document_root=settings.STATIC_URL
         )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
