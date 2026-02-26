from modeltranslation.translator import TranslationOptions, register

from dashboard.models import Circuit


@register(Circuit)
class CircuitTranslation(TranslationOptions):
    fields = ["name"]
