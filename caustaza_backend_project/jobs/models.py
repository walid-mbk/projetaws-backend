from django.db import models
from django.utils.translation import gettext_lazy as _


class Job(models.Model):
    title = models.CharField(_("title"), max_length=255)
    subtitle = models.CharField(_("subtitle"), max_length=255, blank=True)
    meta_title = models.CharField(_("meta title"), max_length=255, blank=True)
    meta_description = models.CharField(_("meta description"), max_length=255, blank=True)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        verbose_name = _("job")
        verbose_name_plural = _("job")

    def __str__(self):
        return self.title
