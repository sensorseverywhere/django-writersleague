from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from .forms import LoginForm, UpdateAccountForm, UserRegistrationForm

from .models import CustomUser
from stories.models import Story


class AccountView(TemplateView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/details.html'


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User logged in')
                else:
                    return HttpResponse('Account disabled')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


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

            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def dashboard(request):
    stories = Story.objects.filter(author=request.user)

    return render(request, 'account/dashboard.html', {'section': 'dashboard', 'stories': stories})


@login_required
def update_account(request):
    
    if request.method == 'POST':
        update_account_form = UpdateAccountForm(instance=request.user, data=request.POST)

        if update_account_form.is_valid():
            update_account_form.save()
            return HttpResponseRedirect(reverse('account:account_details'))
    else:
        update_account_form = UpdateAccountForm(instance=request.user)
    
    return render(request, 'account/update.html', {'update_account_form': update_account_form})
