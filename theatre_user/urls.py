from django.urls import path
from theatre_user.views import RegisterUserView,ManageUserView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
]

app_name = 'user'