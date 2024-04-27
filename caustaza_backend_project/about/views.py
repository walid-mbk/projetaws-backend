from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import About
from .serializers import AboutSerializer


class AboutViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("about")
        if queryset is None:
            queryset = About.objects.all()[:1]
            cache.set("about", queryset, 60)
        serializer = AboutSerializer(queryset, many=True)
        return Response(serializer.data)
