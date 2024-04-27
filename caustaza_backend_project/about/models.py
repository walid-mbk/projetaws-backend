from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), max_length=255, blank=True)
    meta_title = models.CharField(_("meta title"), max_length=255, blank=True)
    meta_description = models.CharField(_("meta description"), max_length=255, blank=True)
    description = models.TextField(_("description"), blank=True)
    long_description = models.TextField(_("long description"), blank=True)

    class Meta:
        verbose_name = _("about")
        verbose_name_plural = _("about")

    def __str__(self):
        return self.title
