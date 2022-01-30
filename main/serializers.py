from rest_framework import serializers

from main.models import Pesticide, ImportRecord, Storage, \
    Room, Preparation


class ImportFileSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)

    def create(self, validated_data):
        return ImportRecord.objects.create(**validated_data)


class PesticideImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = '__all__'


class StorageImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class RoomImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PreparationImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preparation
        fields = '__all__'
