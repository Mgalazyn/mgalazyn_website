from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill, Inbox


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class':'input', 'placeholder': 'Add first name'})

        self.fields['email'].widget.attrs.update({'class':'input', 'placeholder': 'Add email'})

        self.fields['username'].widget.attrs.update({'class':'input', 'placeholder': 'Add username'})

        self.fields['password1'].widget.attrs.update({'class':'input', 'placeholder': 'Type in password'})

        self.fields['password2'].widget.attrs.update({'class':'input', 'placeholder': 'Confirm password'})


class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 
                    'short_intro', 'profile_image', 
                    'social_github', 'social_linkedin', 'social_website']
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

        
    #     for name, field in self.fields.items():
    #         field.widget.update({'class': 'input'})

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})

        self.fields['email'].widget.attrs.update({'class':'input'})

        self.fields['username'].widget.attrs.update({'class':'input'})

        self.fields['location'].widget.attrs.update({'class':'input'})

        self.fields['bio'].widget.attrs.update({'class':'input'})

        self.fields['short_intro'].widget.attrs.update({'class':'input'})

        self.fields['profile_image'].widget.attrs.update({'class':'input'})

        self.fields['social_github'].widget.attrs.update({'class':'input'})

        self.fields['social_linkedin'].widget.attrs.update({'class':'input'})

        self.fields['social_website'].widget.attrs.update({'class':'input'})


class SkillForm(ModelForm):

    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})

        self.fields['description'].widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    
    class Meta:
        model = Inbox
        fields = ['name', 'email', 'subject', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class':'input'})

        self.fields['email'].widget.attrs.update({'class': 'input'})

        self.fields['subject'].widget.attrs.update({'class': 'input'})

        self.fields['body'].widget.attrs.update({'class': 'input'})
