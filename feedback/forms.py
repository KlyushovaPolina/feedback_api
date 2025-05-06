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
        if file:
            max_size = 5 * 1024 * 1024
            if file.size > max_size:
                raise forms.ValidationError("Файл слишком большой. Максимальный размер: 5 МБ.")
        return file

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description.strip():
            raise forms.ValidationError("Описание не может быть пустым.")
        return description