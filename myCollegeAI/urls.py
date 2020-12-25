from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

from profiles.views.authentication import LoginView, RegisterView

admin.site.site_header = 'My College AI'
admin.site.site_title = 'My College AI'
admin.site.index_title = 'AI Aggregator Repository'


def serve_home(request):
    return render(request, 'pages/public/home.html')


urlpatterns = [
  path('admin/', admin.site.urls),
  path('college/', include('college.urls'), name='college'),
  path('login/', LoginView.as_view(), name='login'),
  path('register/', RegisterView.as_view(), name='register'),
  path('', serve_home),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
