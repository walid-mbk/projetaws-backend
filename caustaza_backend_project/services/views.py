from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Service
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("service")
        if queryset is None:
            queryset = Service.objects.all()
            cache.set("service", queryset, 60)
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)
