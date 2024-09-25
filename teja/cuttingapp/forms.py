from django import forms

from .models import *


class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)
            


class appointmentform(forms.ModelForm):
     class Meta:
         model=appointmentmodel
         fields='__all__'
         widgets = {
            'date':XYZ_DateInput(format=["%Y-%m-%d"],),
        }


