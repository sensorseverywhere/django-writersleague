import logging

from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import ContactForm
from user.forms import UserRegistrationForm
from .models import ContentBlock
from stories.models import Story

logger = logging.getLogger(__name__)


class ComingSoonPageView(TemplateView):
    template_name = 'pages/coming-soon.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home'] = ContentBlock.objects.all()
        context['stories'] = Story.objects.all()
        context['user_form'] = UserRegistrationForm()
        return context


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['contents'] = ContentBlock.objects.all()
        return context


class ContactPageView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("thanks")

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)


class ThanksPageView(TemplateView):
    template_name = 'pages/thanks.html'
