from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class':'input', 'placeholder': 'Add first name'})

        self.fields['email'].widget.attrs.update({'class':'input', 'placeholder': 'Add email'})

        self.fields['username'].widget.attrs.update({'class':'input', 'placeholder': 'Add username'})

        self.fields['password1'].widget.attrs.update({'class':'input', 'placeholder': 'Type in password'})

        self.fields['password2'].widget.attrs.update({'class':'input', 'placeholder': 'Confirm password'})

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.atrrs.update({'class': 'input'})

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location', 'bio', 
                    'short_intro', 'profile_image', 
                    'social_github', 'social_linkedin', 'social_website']