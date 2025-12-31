from django import forms
from .models import Moment

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = [
            "title",
            "description",
            "media",
            "memory_date",
            "is_annual",
        ]
        widgets = {
            "memory_date": forms.DateInput(attrs={"type": "date"})
        }
