import pandas as pd
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, MultiPartParser

from main.serializers import ImportFileSerializer
from main.import_excel import import_pesticide, import_storage, \
    import_room, import_preparation


class PesticideImportView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_pesticide(df)

        return Response(status=status.HTTP_201_CREATED)


class StorageImportView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_storage(df)

        return Response(status=status.HTTP_201_CREATED)


class RoomImportView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_room(df)

        return Response(status=status.HTTP_201_CREATED)


class PreparationImportView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ImportFileSerializer
    parser_classes = (FormParser, MultiPartParser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        import_record = serializer.save()

        df = pd.read_excel(import_record.file.path)
        import_preparation(df)

        return Response(status=status.HTTP_201_CREATED)
