from django.db import models


class TeamMember(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=250, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to="teams/teammembers", blank=True)

    class Meta:
        managed = True
        db_table = "team_members"

    def __str__(self):
        return self.name


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    teammember = models.ManyToManyField(
        TeamMember,
    )

    class Meta:
        managed = True
        db_table = "team"

    def __str__(self):
        return self.title
