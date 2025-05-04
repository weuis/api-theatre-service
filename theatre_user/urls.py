from django.urls import path
from theatre_user.views import RegisterUserView, CreateTokenView, ManageUserView


urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path("login/", CreateTokenView.as_view(), name="token"),
    path('me/', ManageUserView.as_view(), name='manage-user'),
]

app_name = 'user'