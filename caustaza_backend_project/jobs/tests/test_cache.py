from unittest.mock import patch

from django.core.cache import cache

from caustaza_backend_project.jobs.tests.test_setup import JobsSetup
from caustaza_backend_project.jobs.views import JobsViewSet


class JobsCacheTestCase(JobsSetup):
    def test_cache(self):
        # Verify that the Job object is not in the cache
        self.assertIsNone(cache.get("job"))

        # Retrieve the Job object using the view
        view = JobsViewSet.as_view({"get": "list"})
        request = self.factory.get("/job/")
        response = view(request)
        data = response.data

        # Verify that the Job object is now in the cache
        self.assertIsNotNone(cache.get("job"))

        # Mock the cache.get method to return the cached Job object
        with patch("django.core.cache.cache.get", return_value=data):
            # Retrieve the Job object again using the view
            request = self.factory.get("/job/")
            response = view(request)
            response = response.data[:1]
            # Verify that the Job object was retrieved from the cache
            self.assertEqual(data, response)
