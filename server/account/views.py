from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import LoginForm, UpdateAccountForm, UpdateProfileForm, UpdateAddressForm, UserRegistrationForm

from .models import Address, CustomUser, Profile
from stories.models import Story


class AccountView(TemplateView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/details.html'


class ProfileView(TemplateView):
    model = Profile
    context_object_name = 'user'
    template_name = 'profile/details.html'


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # set_password hashes the password
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            # Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    
    stories = Story.objects.filter(author=request.user)

    return render(request, 'account/dashboard.html', {'stories': stories})


@login_required
def update_account(request):
    
    if request.method == 'POST':
        update_account_form = UpdateAccountForm(instance=request.user, data=request.POST)
        update_address_form = UpdateAddressForm(instance=request.user, data=request.POST)

        if update_account_form.is_valid() and update_address_form.is_valid():
            update_account_form.save()
            update_address_form.save()

            return HttpResponseRedirect('account/details.html')
    else:
        update_account_form = UpdateAccountForm(instance=request.user)
        update_address_form = UpdateAddressForm(instance=request.user)
    
    return render(request, 'account/update.html', {
                                            'update_account_form': update_account_form,
                                            'update_address_form': update_address_form
                                            })


@login_required
def update_profile(request):
    if request.method == 'POST':
        update_account_form = UpdateAccountForm(instance=request.user, data=request.POST)
        update_profile_form = UpdateProfileForm(instance=request.user.profile, data=request.POST)

        if update_account_form.is_valid() and update_profile_form.is_valid():
            update_account_form.save()
            update_profile_form.save()
            return HttpResponseRedirect(reverse('profile_details'))
    else:
        update_account_form = UpdateAccountForm(instance=request.user)
        update_profile_form = UpdateProfileForm(instance=request.user.profile)
    
    return render(request, 'profile/update.html', { 
                                        'update_account_form': update_account_form,
                                        'update_profile_form': update_profile_form })
