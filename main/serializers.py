from rest_framework import serializers

from main.models import CommonPesticide, ImportRecord


# class CitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = '__all__'


class ImportFileSerializer(serializers.Serializer):
    file = serializers.FileField(write_only=True)

    def create(self, validated_data):
        return ImportRecord.objects.create(**validated_data)


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonPesticide
        fields = '__all__'



