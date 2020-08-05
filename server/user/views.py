from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from rest_framework import generics

from .forms import UpdateAccountForm, UserRegistrationForm
from .models import CustomUser
from .serializers import CustomUserSerializer

from stories.models import Story


class AccountView(TemplateView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/details.html'


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
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    stories = Story.objects.filter(author=request.user)
    return render(request, 'user/dashboard.html', {'stories': stories, 'user': request.user})


@login_required
def update_account(request):
    if request.method == 'POST':
        update_account_form = UpdateAccountForm(instance=request.user, data=request.POST)

        if update_account_form.is_valid():
            update_account_form.save()

            return HttpResponseRedirect(reverse('dashboard'))
    else:
        update_account_form = UpdateAccountForm(instance=request.user)

    return render(request, 'account/update.html', {
                                            'update_account_form': update_account_form
                                            })


@login_required
def update_profile(request):
    if request.method == 'POST':
        update_account_form = UpdateAccountForm(instance=request.user, data=request.POST)
        # update_profile_form = UpdateProfileForm(instance=request.user.profile, data=request.POST)

        if update_account_form.is_valid():
            update_account_form.save()
            return HttpResponseRedirect(reverse('profile_details'))
    else:
        update_account_form = UpdateAccountForm(instance=request.user)

    return render(request, 'profile/update.html', {
                                                    'update_account_form': update_account_form
                                                  })


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
