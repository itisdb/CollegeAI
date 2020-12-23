from django.urls import path

from college.views.public import IndividualCollegeView, CollegesView

urlpatterns = [
    path('list/', CollegesView.as_view(), name='list'),
    path('<slug>/', IndividualCollegeView.as_view(), name='individual')
]
