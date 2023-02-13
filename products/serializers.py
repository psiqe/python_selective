from rest_framework import serializers
from .models import Games

class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['id', 'name', 'price', 'score', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data: dict) -> Games:
        return Games.objects.create(**validated_data)