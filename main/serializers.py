from rest_framework import serializers

from main.models import Pesticide, ImportRecord


class ImportFileSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)

    def create(self, validated_data):
        return ImportRecord.objects.create(**validated_data)


class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = '__all__'



