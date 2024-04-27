from rest_framework import status

from .test_setup import TeamSetup


class TestTeamViews(TeamSetup):
    """Test views for Team app."""

    def test_team_page(self):
        """Test that the API returns a list of teams with the correct data."""

        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "team")
        self.assertEqual(len(response.data), 1)

        team_data = response.data[0]
        self.assertEqual(team_data["title"], "Team A")
        self.assertEqual(team_data["subtitle"], "Subtitle for Team A")
        self.assertEqual(team_data["description"], "Description for Team A")

        # team_member_data = team_data["teammember"]
        # self.assertEqual(len(team_member_data), 2)

        # team_member1_data = team_member_data[0]
        # self.assertEqual(team_member1_data["name"], "John Doe")
        # self.assertEqual(team_member1_data["designation"], "Developer")
        # self.assertEqual(team_member1_data["location"], "New York")
        # self.assertEqual(team_member1_data["description"], "Team member 1 description")
        # self.assertEqual(os.path.basename(team_member1_data["image"]),  self.test_image.name)

        # team_member2_data = team_member_data[1]
        # self.assertEqual(team_member2_data["name"], "Jane Smith")
        # self.assertEqual(team_member2_data["designation"], "Designer")
        # self.assertEqual(team_member2_data["location"], "London")
        # self.assertEqual(team_member2_data["description"], "Team member 2 description")
        # self.assertEqual(os.path.basename(team_member2_data["image"]),  self.test_image.name)
