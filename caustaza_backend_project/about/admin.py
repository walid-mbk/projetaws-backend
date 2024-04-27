from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from .models import About


@admin.register(About)
class AboutAdmin(TabbedTranslationAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("title", "subtitle", "description", "long_description"),
            },
        ),
        (
            _("SEO"),
            {
                "fields": ("meta_title", "meta_description"),
            },
        ),
    ]
