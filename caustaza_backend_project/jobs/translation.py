from modeltranslation.translator import TranslationOptions, translator

from caustaza_backend_project.jobs.models import Job


class JobTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "meta_title", "meta_description", "description")


translator.register(Job, JobTranslationOptions)
