from rest_framework import serializers
from .models import State, City, PolicyArea, Staff, Organization


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('__all__')
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')
        
class PolicyAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyArea
        fields = ('__all__')
            