from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'source_link', 'tags', 'featured_image']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})

        self.fields['description'].widget.attrs.update({'class':'input', 'placeholder': 'Add text'})

        self.fields['source_link'].widget.attrs.update({'class':'input', 'placeholder': 'Add link'})
        

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with you vote'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['body'].lable = ['Place your vote']
        # self.fields['value'].lable = ['Add a comment with you vote']
        
        self.fields['body'].widget.attrs.update({'class':'input', 'placeholder': 'Add comment'})
        self.fields['value'].widget.attrs.update({'class':'input'})
