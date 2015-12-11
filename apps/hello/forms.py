from django import forms
from models import Contact
from apps.hello.widgets import CalendarWidget


class ContactForm(forms.ModelForm):
    birth_date = forms.DateField(widget=CalendarWidget(
        params="dateFormat: 'yy-mm-dd', changeYear: true,\
         changeMonth: true, yearRange: '1950:2016'",
        attrs={'class': 'datepicker'}))

    class Meta:
        model = Contact
        widgets = {
            'bio': forms.Textarea(attrs={'cols': 50, 'rows': 7}),
            'other': forms.Textarea(attrs={'cols': 50, 'rows': 7})
        }
