from django.urls import path

from openday.api.views import users

urlpatterns = [
    path('user/', users.UserDetail.as_view(), name='user'),

]
