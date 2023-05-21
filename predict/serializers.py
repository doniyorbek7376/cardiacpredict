from rest_framework import serializers
from .models import PredictionRequest

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionRequest
        fields = '__all__'