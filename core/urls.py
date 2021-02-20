from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet

router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]