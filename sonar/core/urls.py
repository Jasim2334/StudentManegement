from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import StudentViewset

app_name = "core"

router = DefaultRouter()
router.register("", StudentViewset)

urlpatterns = [
    path("", include(router.urls)),
]