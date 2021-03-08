from django.urls import path

from profiles.views.profile import Dashboard, EditUserProfileView, UpdatePassword, ForgotPassword, EnterEmail

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('edit-profile/', EditUserProfileView.as_view(), name='edit-profile'),
    path('update-password/', UpdatePassword.as_view(), name='edit-password'),
    path('reset-password/<str:username>/<str:otp>',ForgotPassword.as_view(),name = 'forgot-password'),
    path('forgot-password/',EnterEmail.as_view(),name = 'enter-email'),
]
