from django import forms

from contact.models import Contact, ContactMatter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()


class ContactMatterForm(forms.ModelForm):
    matter = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = ContactMatter
        exclude = ('contact',)
