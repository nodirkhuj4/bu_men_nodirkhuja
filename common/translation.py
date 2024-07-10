from modeltranslation.translator import register, TranslationOptions
from .models import Settings


@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = ('location_text',)

