from django.urls import path
from theatre_user.views import RegisterUserView, ManageUserView, LoginUserView

from rest_framework.authtoken import views


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path("login/", LoginUserView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
]

app_name = 'user'