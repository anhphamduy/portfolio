from contact.models import ContactPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(ContactPage)
class ContactPageTR(TranslationOptions):
    fields = ()
