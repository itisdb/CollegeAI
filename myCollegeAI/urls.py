from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from base import views as base_views

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
  path('', base_views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
