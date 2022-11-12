from django.forms import ModelForm
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'source_link', 'tags', 'featured_image']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add text'})

        self.fields['source_link'].widget.attrs.update({'class':'input', 'placeholder': 'Add link'})
        