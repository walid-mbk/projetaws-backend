from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from caustaza_backend_project.teams.models import Team, TeamMember


class TeamSetup(APITestCase):
    def setUp(self):
        self.index_url = reverse("api:teams-list")
        self.client = APIClient()
        self.factory = APIRequestFactory()

        # Create Team Members
        self.test_image = SimpleUploadedFile(
            name="test_image.jpg",
            content=open("caustaza_backend_project/teams/tests/test_image.jpeg", "rb").read(),
            content_type="image/jpeg",
        )
        self.team_member1 = TeamMember.objects.create(
            name="John Doe",
            designation="Developer",
            location="New York",
            description="Team member 1 description",
            image=self.test_image,
        )
        self.team_member2 = TeamMember.objects.create(
            name="Jane Smith",
            designation="Designer",
            location="London",
            description="Team member 2 description",
            image=self.test_image,
        )
        # Create Team
        self.team = Team.objects.create(
            title="Team A",
            subtitle="Subtitle for Team A",
            description="Description for Team A",
        )
        # Add team members to the team
        self.team.teammember.add(self.team_member1, self.team_member2)

    def tearDown(self):
        return super().tearDown()
