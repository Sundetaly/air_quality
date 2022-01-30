from django.urls import include, path
from rest_framework.routers import DefaultRouter

from main.views import PesticideImportView, StorageImportView, \
    RoomImportView, PreparationImportView

app_name = 'main'

# router = DefaultRouter()
# router.register(r'pesticide', PesticideViewSet, basename='pesticide')

urlpatterns = [
    # path('', include(router.urls)),
    path('pecticide-import/', PesticideImportView.as_view(), name='district-import'),
    path('storage-import/', StorageImportView.as_view(), name='storage-import'),
    path('room-import/', RoomImportView.as_view(), name='room-import'),
    path('preparation-import/', PreparationImportView.as_view(), name='preparation-import'),
]
