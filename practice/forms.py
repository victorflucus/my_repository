import datetime
from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AddNewProject(forms.Form):
    title = forms.CharField(max_length=250, help_text="Enter the name of the project here.")
    details = forms.CharField(widget=forms.Textarea)
    due_date = forms.DateField(help_text="Enter the date at which you would like this project to be completed.")
    estimated_hours = forms.DecimalField(max_digits=10, decimal_places=3)

    def clean_due_date(self):
        date_data = self.cleaned_data['due_date']

        # check to see if this date is in the past:
        if date_data < datetime.date.today():
            raise ValidationError(_('Invalid date - Date entered is in the past'))

        return date_data

    def clean_tittle(self):
        title_data = self.cleaned_data['title']
        return title_data

    def clean_details(self):
        details_data = self.cleaned_data['details']
        return details_data

    def clean_estimated_hours(self):
        estimated_hours_data = self.cleaned_data['estimated_hours']
        return estimated_hours_data

class TextCountAnalysis(forms.Form):
    title = forms.CharField(max_length=250, help_text="Enter a title for your entry (Optional)")
    paragraph = forms.CharField(min_length=50, widget=forms.Textarea, help_text="Enter a paragraph for analysis. This "
                                                                                "is required and must be 50 "
                                                                                "characters at minimum.",
                                required=True)
    source = forms.CharField(max_length=250,  widget=forms.Textarea, help_text="Enter the source of your entry (Optional)")

    def clean_tittle(self):
        title_data = self.cleaned_data['title']
        return title_data

    def clean_source(self):
        source_data = self.cleaned_data['source']
        return source_data

    def clean_paragraph(self):
        paragraph_data = self.cleaned_data['paragraph']
        return paragraph_data