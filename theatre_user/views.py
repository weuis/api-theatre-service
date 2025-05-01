from rest_framework import generics
from rest_framework.permissions import AllowAny
from theatre_user.models import CustomUser
from theatre_user.serializer import UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CreateTokenView(ObtainAuthToken):
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES