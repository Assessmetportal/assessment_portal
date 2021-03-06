from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from interview.models import Interview, Response
from djoser.serializers import UserSerializer


class InterviewCreateSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = (
            'id',
            'theme',
            'interviewer',
            'interviewed',
            'date_of_interview',
            'is_active',
        )


class ResponseSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = (
            'id',
            'interview',
            'final_grade',
            'response',
        )
