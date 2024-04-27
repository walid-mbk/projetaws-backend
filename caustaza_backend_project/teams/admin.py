from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Team, TeamMember


@admin.register(Team)
class TeamAdmin(TabbedTranslationAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("title", "subscription", "description", "teammember"),
            },
        ),
    ]


@admin.register(TeamMember)
class TeamMembersAdmin(TabbedTranslationAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("name", "designation", "location", "description"),
            },
        ),
    ]

    readonly_fields = ("image_preview",)

    @admin.display(description=_("Image Preview"))
    def image_preview(self, obj):
        if obj.image:
            return format_html('<div style="max-width: 300px;">{}</div>', obj.image.admin_thumbnail)
        else:
            return _("No image found")
