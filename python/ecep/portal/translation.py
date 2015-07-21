from modeltranslation.translator import translator, TranslationOptions
from portal.models import Location

class LocationTranslationOptions(TranslationOptions):
    fields = ('q_stmt', 'enrollment', 'open_house', 'curriculum',)

translator.register(Location, LocationTranslationOptions)