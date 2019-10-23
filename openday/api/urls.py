from django.urls import path

from openday.api.views import users, enrollments

urlpatterns = [
    path('user/', users.UserDetail.as_view(), name='user'),
    path('enroll/', enrollments.EnrollUserView.as_view(), name='enroll'),
    path('events/', enrollments.EventView.as_view(), name='events'),
]
