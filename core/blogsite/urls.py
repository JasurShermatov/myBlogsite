from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("superadmin/", admin.site.urls),
    path("", include("main_app.urls")),  # Asosiy sahifa
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
