from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from caustaza_backend_project.jobs.models import Job


class JobsSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("api:jobs-list")
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.job = Job.objects.create(
            title="Job",
            title_en="Job",
            title_fr="Job",
            subtitle="This is the job page subtitle.",
            subtitle_en="This is the job page subtitle.",
            subtitle_fr="Ceci est le sous-titre de la page Job.",
            meta_title="Job meta title",
            meta_title_en="Job meta title",
            meta_title_fr="Titre méta Job",
            meta_description="This is the job page meta description.",
            meta_description_en="This is the job page meta description.",
            meta_description_fr="Ceci est la description méta de la page Job.",
            description="This is the job page description.",
            description_en="This is the job page description.",
            description_fr="Ceci est la description de la page Job.",
        )
        self.job.save()

    def tearDown(self):
        return super().tearDown()
