from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

admin.site.site_header = 'My College AI'
admin.site.site_title = 'My College AI'
admin.site.index_title = 'AI Aggregator Repository'


def serve_home(request):
    return render(request, 'pages/public/home.html')


def serve_login(request):
    return render(request, 'pages/auth/login.html')


def serve_register(request):
    return render(request, 'pages/auth/register.html')


urlpatterns = [
  path('admin/', admin.site.urls),
  path('college/', include('college.urls'), name='college'),
  path('login/', serve_login),
  path('register/', serve_register),
  path('', serve_home),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
