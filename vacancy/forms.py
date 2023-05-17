from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'description', 'budget', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Job Title"
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Job Description"
            }),
            'budget': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "budget"
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "data",
            }),
        }