from django.urls import path
from theatre_user.views import RegisterUserView, CreateTokenView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path("login/", CreateTokenView.as_view(), name="token")
]

app_name = 'user'