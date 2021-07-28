from django.contrib.auth import get_user_model
from rest_framework import mixins, generics, viewsets

from users.models import Profile
from users.api.serializers import ProfileSerializer

User = get_user_model()


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     generics.GenericAPIView,
                     viewsets.ViewSet):
    """
        retrieve:
            Return a profile.

        list:
            Return all profiles, ordered by most recently joined.

        partial_update:
            Update one or more fields on an existing profile.

        update:
            Update a profile.
        """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_queryset(self):
        return Profile.objects \
            .select_related('user') \
            .all()
