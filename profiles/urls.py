from django.urls import path

from profiles.views.profile import Dashboard,EditUserProfileView,UpdatePassword

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('edit-profile/', EditUserProfileView.as_view(), name='edit-profile'),
    path('update-password/', UpdatePassword.as_view(), name='edit-password'),
]
