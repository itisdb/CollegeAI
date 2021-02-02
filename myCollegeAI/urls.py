from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from base import views as base_views

from leads.views.public import ContactUs

from profiles.views.authentication import (
    LoginView,
    LogoutView,
    RegisterView
)

from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

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
  path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='pages/auth/reset-password.html'),
        name ='password_reset'),
  path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='pages/auth/reset-password-done.html'),
        name ='password_reset_done'),
  path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='pages/auth/reset-password-confirm.html'),
        name ='password_reset_confirm'),
  path('activate/<uidb64>/<token>',VerificationView.as_view(),name='activate')
  path('contact/', ContactUs.as_view(), name='contact'),
  path('', base_views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    ) + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
