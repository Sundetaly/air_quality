from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import PesticideViewSet, DistrictImportFileView

app_name = 'main'

router = DefaultRouter()
router.register(r'pesticide', PesticideViewSet, basename='pesticide')

urlpatterns = [
    path('', include(router.urls)),
    path('district-import/', DistrictImportFileView.as_view(), name='district-import')
]
