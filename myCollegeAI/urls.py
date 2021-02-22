from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views as base_views

from leads.views.public import ContactUs

from profiles.views.authentication import (
    LoginView,
    LogoutView,
    RegisterView
)

handler404 = 'base.views.custom_not_found_error'
handler500 = 'base.views.custom_internal_error'
handler403 = 'base.views.custom_not_found_error'
handler400 = 'base.views.custom_not_found_error'

urlpatterns = [
  path('admin/', admin.site.urls),
  path('college/', include(('college.urls', 'college'), namespace='college')),
  path('profile/', include(('profiles.urls', 'profile'), namespace='profile')),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('register/', RegisterView.as_view(), name='register'),
  path('contact/', ContactUs.as_view(), name='contact'),
  path('', base_views.home, name='home'),
  path('refer', base_views.refer, name='refer'),
  path('about', base_views.about, name='about'),
  path('contact', base_views.contact, name='contact'),
  path('career', base_views.career, name='career'),
  path('advertising', base_views.advertising, name='advertising'),
  path('terms', base_views.terms, name='terms'),
  path('privacy',  base_views.privacy, name='privacy'),
  path('social', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
