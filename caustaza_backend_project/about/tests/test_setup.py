from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from caustaza_backend_project.about.models import About


class AboutSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("api:about-list")
        self.client = APIClient()
        self.factory = APIRequestFactory()

        self.about = About.objects.create(
            title="About",
            title_en="About",
            title_fr="À propos",
            subtitle="This is the about page subtitle.",
            subtitle_en="This is the about page subtitle.",
            subtitle_fr="Ceci est le sous-titre de la page À propos.",
            meta_title="About meta title",
            meta_title_en="About meta title",
            meta_title_fr="Titre méta À propos",
            meta_description="This is the about page meta description.",
            meta_description_en="This is the about page meta description.",
            meta_description_fr="Ceci est la description méta de la page À propos.",
            description="This is the about page description.",
            description_en="This is the about page description.",
            description_fr="Ceci est la description de la page À propos.",
            long_description="This is the about page long description.",
            long_description_en="This is the about page long description.",
            long_description_fr="Ceci est la longue description de la page À propos.",
        )
        self.about.save()

    def tearDown(self):
        return super().tearDown()
