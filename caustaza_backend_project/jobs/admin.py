from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from caustaza_backend_project.jobs.models import Job


@admin.register(Job)
class AboutAdmin(TabbedTranslationAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("title", "subtitle", "description"),
            },
        ),
        (
            _("SEO"),
            {
                "fields": ("meta_title", "meta_description"),
            },
        ),
    ]
