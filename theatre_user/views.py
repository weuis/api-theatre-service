from rest_framework import generics
from rest_framework.permissions import AllowAny
from theatre_user.models import CustomUser
from theatre_user.serializer import UserSerializer


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]