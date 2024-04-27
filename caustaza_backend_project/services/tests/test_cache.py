from unittest.mock import patch

from django.core.cache import cache

from caustaza_backend_project.services.tests.test_setup import ServiceSetup
from caustaza_backend_project.services.views import ServiceViewSet


class ServiceCacheTestCase(ServiceSetup):
    def test_cache(self):
        # Verify that the Service object is not in the cache
        self.assertIsNone(cache.get("service"))

        # Retrieve the Service object using the view
        view = ServiceViewSet.as_view({"get": "list"})
        request = self.factory.get("/service/")
        response = view(request)
        data = response.data

        # Verify that the Service object is now in the cache
        self.assertIsNotNone(cache.get("service"))

        # Mock the cache.get method to return the cached Service object
        with patch("django.core.cache.cache.get", return_value=data):
            # Retrieve the Service object again using the view
            request = self.factory.get("/service/")
            response = view(request)
            new_data = response.data
            # Verify that the Service object was retrieved from the cache
        # Verify that the Service object was retrieved from the cache
        self.assertEqual(len(new_data), 1)
        self.assertEqual(new_data[0]["title"], data[0]["title"])
        self.assertEqual(new_data[0]["short_content"], data[0]["short_content"])
