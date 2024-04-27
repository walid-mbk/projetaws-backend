from unittest.mock import patch

from django.core.cache import cache

from caustaza_backend_project.teams.views import TeamViewSet

from .test_setup import TeamSetup


class TestTeamCache(TeamSetup):
    def test_cache(self):
        # Verify that the Team object is not in the cache
        self.assertIsNone(cache.get("teams"))

        # Retrieve the Team object using the view
        view = TeamViewSet.as_view({"get": "list"})
        request = self.factory.get("/team/")
        response = view(request)
        data = response.data

        # Verify that the Team object is now in the cache
        self.assertIsNotNone(cache.get("teams"))

        # Mock the cache.get method to return the cached Team object
        with patch("django.core.cache.cache.get", return_value=data):
            # Retrieve the Team object again using the view
            request = self.factory.get("/team/")
            response = view(request)
            new_data = response.data

            # Verify that the Team object was retrieved from the cache
            self.assertEqual(len(new_data), 1)
            self.assertEqual(new_data[0]["title"], data[0]["title"])
            self.assertEqual(new_data[0]["subtitle"], data[0]["subtitle"])
            self.assertEqual(new_data[0]["description"], data[0]["description"])
