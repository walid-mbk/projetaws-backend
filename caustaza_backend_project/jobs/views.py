from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Job
from .serializers import JobsSerializer


class JobsViewSet(viewsets.ViewSet):
    authentication_classes = []

    def list(self, request):
        queryset = cache.get("job")
        if queryset is None:
            queryset = Job.objects.all()[:1]
            cache.set("job", queryset, 60)
        serializer = JobsSerializer(queryset, many=True)
        return Response(serializer.data)
