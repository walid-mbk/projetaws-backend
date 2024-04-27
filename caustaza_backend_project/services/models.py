from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(_("title"), max_length=255)
    short_content = models.CharField(_("short content"), max_length=255)
    image = models.ImageField(_("image"), upload_to="services")

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("service")

    def __str__(self):
        return self.title

    def image_tag(self):
        return '<img href="{0}" src="{0}" width="150" height="150" />'.format(self.image.url)

    image_tag.allow_tags = True
    image_tag.short_description = "Image"
