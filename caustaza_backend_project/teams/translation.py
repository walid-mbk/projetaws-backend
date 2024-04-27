from modeltranslation.translator import TranslationOptions, translator

from .models import Team, TeamMember


class TeamTranslationOptions(TranslationOptions):
    fields = ("title", "subtitle", "description")


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ("designation", "description")


translator.register(Team, TeamTranslationOptions)
translator.register(TeamMember, TeamMemberTranslationOptions)
