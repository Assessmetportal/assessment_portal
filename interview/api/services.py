from django.contrib.auth import get_user_model
from interview.api.serializers import ResponseSerializer, InterviewCreateSerializer
from interview.models import Interview
from interview.models import Response as resp
from rest_framework import status, mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()


class InterviewList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView,
                    viewsets.ViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewCreateSerializer

    def get_queryset(self):
        where_interviewer = Interview.objects.select_related('interviewer') \
            .filter(interviewer=self.request.user)
        where_interviewed = Interview.objects.select_related('interviewer') \
            .filter(interviewed=self.request.user)
        return where_interviewed | where_interviewer


class ResponseList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   generics.GenericAPIView,
                   viewsets.ViewSet):
    queryset = resp.objects.all()
    serializer_class = ResponseSerializer

    def get_queryset(self):
        interview = Interview.objects.filter(interviewed=self.request.user)
        return resp.objects.filter(interview__in=interview)
