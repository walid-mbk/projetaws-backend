from modeltranslation.translator import TranslationOptions, translator

from .models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ("title", "short_content")


translator.register(Service, ServiceTranslationOptions)
