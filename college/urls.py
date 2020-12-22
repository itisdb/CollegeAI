from django.urls import path

from college.views.public import CollegesView

urlpatterns = [
    path('list/', CollegesView.as_view(), name='list')
]
