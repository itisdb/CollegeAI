from django.urls import path

from college.views.public import AddBookmarkView, IndividualCollegeView, CollegesView

urlpatterns = [
    path('list/', CollegesView.as_view(), name='list'),
    path('<slug>/', IndividualCollegeView.as_view(), name='individual'),
    path('bookmark/<slug>/', AddBookmarkView.as_view(), name='bookmark')
]
