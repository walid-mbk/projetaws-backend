from rest_framework import status

from caustaza_backend_project.jobs.tests.test_setup import JobsSetup


class TestViews(JobsSetup):
    """Test views for jobs app."""

    def test_job_page(self):
        """Test that the job page APIs are working with the correct data."""

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Job")

        self.assertEqual(response.data[0]["title"], "Job")
        self.assertEqual(response.data[0]["title_en"], "Job")
        self.assertEqual(response.data[0]["title_fr"], "Job")
        self.assertEqual(response.data[0]["subtitle"], "This is the job page subtitle.")
        self.assertEqual(response.data[0]["subtitle_en"], "This is the job page subtitle.")
        self.assertEqual(response.data[0]["subtitle_fr"], "Ceci est le sous-titre de la page Job.")
        self.assertEqual(response.data[0]["meta_title"], "Job meta title")
        self.assertEqual(response.data[0]["meta_title_en"], "Job meta title")
        self.assertEqual(response.data[0]["meta_title_fr"], "Titre méta Job")
        self.assertEqual(
            response.data[0]["meta_description"],
            "This is the job page meta description.",
        )
        self.assertEqual(
            response.data[0]["meta_description_en"],
            "This is the job page meta description.",
        )
        self.assertEqual(
            response.data[0]["meta_description_fr"],
            "Ceci est la description méta de la page Job.",
        )
        self.assertEqual(response.data[0]["description"], "This is the job page description.")
        self.assertEqual(response.data[0]["description_en"], "This is the job page description.")
        self.assertEqual(response.data[0]["description_fr"], "Ceci est la description de la page Job.")
