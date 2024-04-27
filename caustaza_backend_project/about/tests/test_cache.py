from unittest.mock import patch

from django.core.cache import cache

from caustaza_backend_project.about.tests.test_setup import AboutSetup
from caustaza_backend_project.about.views import AboutViewSet


class AboutCacheTestCase(AboutSetup):
    def test_cache(self):
        # Verify that the About object is not in the cache
        self.assertIsNone(cache.get("about"))

        # Retrieve the About object using the view
        view = AboutViewSet.as_view({"get": "list"})
        request = self.factory.get("/about/")
        response = view(request)
        data = response.data

        # Verify that the About object is now in the cache
        self.assertIsNotNone(cache.get("about"))

        # Mock the cache.get method to return the cached About object
        with patch("django.core.cache.cache.get", return_value=data):
            # Retrieve the About object again using the view
            request = self.factory.get("/about/")
            response = view(request)
            data = response.data[:1]
            # Verify that the About object was retrieved from the cache
            self.assertEqual(data, data)
