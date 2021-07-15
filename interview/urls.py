from django.urls import path, include

from interview.api.services import InterviewList, ResponseList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'interviews', InterviewList, basename='Interview')
router.register(r'responses', ResponseList, basename='Response')
app_name = "interviews"

urlpatterns = router.urls

