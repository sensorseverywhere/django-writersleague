from django import forms

from django.contrib.auth import get_user_model

from .models import CustomUser, Profile


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'user_type')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email',)



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'active')

