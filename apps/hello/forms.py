from django import forms
from  models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 50, 'rows': 7}),
            'other': forms.Textarea(attrs={'cols': 50, 'rows': 7})
        }