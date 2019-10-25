from django.urls import path, re_path

from openday.api.views import users, enrollments

urlpatterns = [
    path('user/', users.UserDetail.as_view(), name='user'),
    re_path(r'enrollments/guest/(?P<email>([^@\s]+@[^@\s]+\.[^@\s]+))/',
            enrollments.EnrollGuestView.as_view(), name='enroll'),
    path('enrollments/', enrollments.EnrollUserView.as_view(), name='enroll'),
    path('enrollments/<id>/', enrollments.EnrollmentDelete.as_view(),
         name='enroll'),
    path('events/', enrollments.EventView.as_view(), name='events'),
]
