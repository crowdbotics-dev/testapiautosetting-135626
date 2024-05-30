from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135626ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135626", Testconnectors135626ViewSet, basename="testconnectors135626"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
