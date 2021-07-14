from collections import namedtuple
from django.urls import path

from college.views.public import AddBookmarkView, ApplyCollegeView, IndividualCollegeView, CollegesView
from college.views.temporary import SEOCollegesView, topCollegesView, tagCollegesView, taglocCollegesView

urlpatterns = [
    path('best-colleges-in-<location>/', SEOCollegesView.as_view(), name='seo-list'),
    path('list-of-all-<college>-colleges-in-India/', topCollegesView.as_view(), name='top-list'),
    path('best-<tag>-colleges-in-<location>/', taglocCollegesView.as_view(), name='tagloc-list'),
    path('<tag>-colleges-in-India/', tagCollegesView.as_view(), name='tag-list'),
    path('list/', CollegesView.as_view(), name='list'),
    path('apply/<college_uuid>/', ApplyCollegeView.as_view(), name='apply'),
    path('<slug>/', IndividualCollegeView.as_view(), name='individual'),
    path('bookmark/<slug>/', AddBookmarkView.as_view(), name='bookmark')
]
