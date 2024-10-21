from rest_framework import serializers
from .models import Source, PhysicalDataSet

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class PhysicalDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalDataSet
        fields = '__all__'
