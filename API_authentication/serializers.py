from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=65, min_length=6, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=2)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    user_type = serializers.CharField(default=3)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'user_type']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=2)
    password = serializers.CharField(max_length=65, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']
