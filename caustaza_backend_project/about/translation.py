from modeltranslation.translator import TranslationOptions, translator

from .models import About


class AboutTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "meta_title", "meta_description", "description", "long_description")


translator.register(About, AboutTranslationOptions)
