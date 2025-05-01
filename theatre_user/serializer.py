from rest_framework import serializers
from theatre_user.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id', 'email', 'username', 'password',
            'first_name', 'last_name', 'phone', 'date_of_birth', 'is_staff'
        )
        read_only_fields = ('id', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 5}
        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
