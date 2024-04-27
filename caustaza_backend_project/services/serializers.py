from rest_framework import serializers

from .models import Service


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Service
        fields = "__all__"
