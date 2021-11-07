from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import CityViewSet, DistrictViewSet, CityImportFileView, DistrictImportFileView

app_name = 'main'

router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'district', DistrictViewSet, basename='district')

urlpatterns = [
    path('', include(router.urls)),
    path('city-import/', CityImportFileView.as_view(), name='city-import'),
    path('district-import/', DistrictImportFileView.as_view(), name='district-import')
]
