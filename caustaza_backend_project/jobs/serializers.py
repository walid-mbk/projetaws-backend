from rest_framework import serializers

from caustaza_backend_project.jobs.models import Job


class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"
