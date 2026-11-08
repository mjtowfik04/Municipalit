from rest_framework import serializers
from .models import Wards

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wards
        fields=('__all__')
        