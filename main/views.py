import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from main.models import Pesticide
from main.serializers import PesticideSerializer, ImportFileSerializer
from main.import_excel import import_district


class PesticideViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Pesticide.objects.all()
    serializer_class = PesticideSerializer
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
