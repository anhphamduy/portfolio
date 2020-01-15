from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


# Create your models here.
class AboutPage(Page):    
    blurb = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('blurb', classname="full")
    ]