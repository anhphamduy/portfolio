from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from wagtail.core.models import Page


# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)


class ContactMatter(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    matter = models.CharField(max_length=1000)


class ContactPage(Page):
    success_messages = {
        'successful_submission': _("Successfully submitted! I will be in touch with you within a couple of days."),
    }

    def serve(self, request):
        from contact.forms import ContactForm, ContactMatterForm
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            contact_matter_form = ContactMatterForm(request.POST)
            
            if contact_form.is_valid() and contact_matter_form.is_valid():
                contact = contact_form.save()

                matter = contact_matter_form.save(commit=False)
                matter.contact = contact

                matter.save()

                messages.success(request, self.success_messages['successful_submission'])

                return redirect(self.url)
        else:
            contact_form = ContactForm()
            contact_matter_form = ContactMatterForm()

        return render(request, 'contact/contact_page.html', {
            'page': self,
            'contact_form': contact_form,
            'contact_matter_form': contact_matter_form
        })
