from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from users.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = (
            'user',
            'role',
            'technical_skills',
            'soft_skills',
            'language_level',
            'avatar',
        )
