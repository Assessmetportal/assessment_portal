from django.contrib.auth import get_user_model
from rest_framework import mixins, generics, viewsets

from users.models import Profile
from users.api.serializers import ProfileSerializer

User = get_user_model()


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView,
                     viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        return Profile.objects \
            .select_related('user') \
            .all()
