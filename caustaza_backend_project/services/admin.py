from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Service


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    tabs = [
        (
            _("General"),
            {
                "fields": ("title", "subtitle", "image_preview"),
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
