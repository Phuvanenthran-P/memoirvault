from django import forms
from .models import Moment

class MomentForm(forms.ModelForm):
    class Meta:
        model = Moment
        fields = [
            "title",
            "description",
            "media",
            "special_date",
            "remind_me",
        ]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters.")
        return title
