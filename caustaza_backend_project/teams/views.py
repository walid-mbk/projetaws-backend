from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Team
from .serializers import TeamSerializer


class TeamViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("teams")
        if queryset is None:
            queryset = Team.objects.all()
            cache.set("teams", queryset, 60)  # Cache 60 sec
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)
