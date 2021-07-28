from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'role',
            'technical_skills',
            'soft_skills',
            'language_level',
            'grade',
            'avatar',
        )
