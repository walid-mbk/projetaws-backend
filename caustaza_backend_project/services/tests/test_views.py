import os

from rest_framework import status

from caustaza_backend_project.services.tests.test_setup import ServiceSetup


class TestViews(ServiceSetup):
    """Test views for About app."""

    def test_service_page(self):
        """Test that the about page APIs are working with the correct data."""

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Service")

        self.assertEqual(response.data[0]["title"], "Services")
        self.assertEqual(response.data[0]["title_en"], "Services")
        self.assertEqual(response.data[0]["title_fr"], "Services")
        self.assertEqual(response.data[0]["short_content"], "This is the services page short_content.")
        self.assertEqual(response.data[0]["short_content_en"], "This is the services page short_content.")
        self.assertEqual(response.data[0]["short_content_fr"], "Ceci est le sous-titre de la page services.")

        self.assertEqual(os.path.basename(response.data[0]["image"]), self.test_image.name)
