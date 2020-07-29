from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ( UserCreationForm as DjangoUserCreationForm )
from django.contrib.auth.forms import UsernameField
from django.core.mail import send_mail
import logging

from django.contrib.auth import get_user_model

from .models import Address, CustomUser

logger = logging.getLogger(__name__)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class WLSignupForm(SignupForm):
    OPTIONS = [
        ("0", "Sponsor"),
        ("1", "Author"),
        ]
        
    user_type = forms.ChoiceField(choices=OPTIONS)

    def signup(self, request):
        print(user)
        # user.user_type = self.cleaned_data['user_type']
        user.save()

        return user


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'user_type')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']

    def send_mail(self):
        logger.info( "Sending signup email for email=%s", self.cleaned_data["email"])
        message = "Welcome{}".format(self.cleaned_data["email"])
        send_mail(
            "Welcome to the Writers League!",
            message,
            "user@thewritersleague.com",
            [self.cleaned_data["email"]],
            fail_silently=True
        )


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')


class UpdateAddressForm(forms.ModelForm):
    class Meta:
        model = Address 
        fields = ('address1', 'address2', 'city', 'country')
