from rest_framework.routers import DefaultRouter
from users.api.services import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='Profile')
app_name = "interviews"

urlpatterns = router.urls
