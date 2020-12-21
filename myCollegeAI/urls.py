from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path


def serve_home(request):
    return render(request, 'pages/public/home.html')


urlpatterns = [
  path('admin/', admin.site.urls),
  path('', serve_home),
]

if settings.DEBUG:
    urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
