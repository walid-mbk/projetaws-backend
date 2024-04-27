from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from caustaza_backend_project.services.models import Service


class ServiceSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("api:services-list")
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.test_image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open("caustaza_backend_project/services/tests/test_image.jpeg", "rb").read(),
            content_type="image/jpeg",
        )

        self.service = Service.objects.create(
            title="Services",
            title_en="Services",
            title_fr="Services",
            short_content="This is the services page short_content.",
            short_content_en="This is the services page short_content.",
            short_content_fr="Ceci est le sous-titre de la page services.",
            image=self.test_image,
        )
        self.service.save()

    def tearDown(self):
        return super().tearDown()
