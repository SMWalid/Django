from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SourceViewSet, PhysicalDataSetViewSet

router = DefaultRouter()
router.register(r'sources', SourceViewSet)
router.register(r'physicaldatasets', PhysicalDataSetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
