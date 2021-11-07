import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from main.models import City, District
from main.serializers import CitySerializer, DistrictSerializer, ImportFileSerializer
from main.import_excel import import_city, import_district


class CityViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'pollution_level_00', 'pollution_level_01', 'pollution_level_02', 'industries')


class CityImportFileView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_city(df)

        return Response(status=status.HTTP_201_CREATED)


class DistrictViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'count_pesticide', 'name_pesticide', 'name_banned_pesticide')


class DistrictImportFileView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_district(df)

        return Response(status=status.HTTP_201_CREATED)
