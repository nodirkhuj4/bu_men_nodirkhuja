from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['email', 'password', 'password2']


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError({"message": "Both password must match"})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({"message": "Email already taken!"})
        
        return attrs

        