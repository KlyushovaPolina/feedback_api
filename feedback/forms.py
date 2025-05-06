from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_type', 'description', 'file']
        widgets = {
            'feedback_type': forms.Select(),
            'description': forms.Textarea(),
        }

    def clean_file(self):
        file = self.cleaned_data.get('file')
        return file