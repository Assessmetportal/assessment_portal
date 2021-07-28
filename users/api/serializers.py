from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from drf_writable_nested import WritableNestedModelSerializer
from users.models import Profile

User = get_user_model()



    class Meta:
        model = Profile
        fields = (
            'role',
            'technical_skills',
            'soft_skills',
            'language_level',
            'avatar',
        )
