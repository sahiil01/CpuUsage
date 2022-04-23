from rest_framework import serializers
from .models import CpuData


class CpuDataSerializer(serializers.Serializer):
    core1 = serializers.CharField(max_length=20)
    core2 = serializers.CharField(max_length=20)
    core3 = serializers.CharField(max_length=20)
    core4 = serializers.CharField(max_length=20)
    cpuSpeed = serializers.CharField(max_length=20)
    ramUsage = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return CpuData.objects.create(**validated_data)
