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
    """
    retrieve:
        Return an interview.

    list:
        Return all interviews, where you were an interviewer or interviewed.

    create:
        Create a new interview.

    delete:
        Remove an existing interview.

    partial_update:
        Update one or more fields on an existing interview.

    update:
        Update a interview.
    """
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
    """
        retrieve:
            Return an response.

        list:
            Return all your responses.

        create:
            Create a new response.

        delete:
            Remove an existing response.

        partial_update:
            Update one or more fields on an existing response.

        update:
            Update a response.
        """
    queryset = resp.objects.all()
    serializer_class = ResponseSerializer

    def get_queryset(self):
        interview = Interview.objects.filter(interviewed=self.request.user)
        return resp.objects.filter(interview__in=interview)
