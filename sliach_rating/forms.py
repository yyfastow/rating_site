from django import forms
from django.core import validators

from . import models


class RatingForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = [
            'name',
            'rate',
            'comment',
        ]
    
    def clean(self):
        cleaned_data = super().clean()
        rate = cleaned_data.get('rate')

        if rate > 10 or rate < 1:
            raise forms.ValidationError(
                "Only rate from 1 to 10, no more no less."
            )
