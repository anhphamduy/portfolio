from about.models import AboutPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(AboutPage)
class AboutPageTR(TranslationOptions):
    fields = (
        'blurb',
    )
