
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from rest_framework import generics

from .forms import UpVoteForm, DownVoteForm
from .models import Story
from .serializers import StorySerializer
from user.models import CustomUser

class StoryListAPIView(generics.ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryCreateAPIView(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoryListView(ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'story/list.html'


class StoryDetailView(DetailView):
    model = Story
    template_name = 'story/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user
            context['num_votes'] = user.num_votes
        context['upvote_form'] = UpVoteForm()
        context['downvote_form'] = DownVoteForm()

        return context


class StoryUpVoteView(LoginRequiredMixin, UpdateView):
    model = Story
    form_class = UpVoteForm
    # template_name = 'story/upvote.html'

    def form_valid(self, form):
        user = CustomUser.objects.get(pk=self.request.user.id)
        num_votes = user.num_votes
        try:
            if num_votes >= 1:
                num_votes = num_votes - 1
                user.num_votes = num_votes
                user.save()
                id = self.object.id
                story = Story.objects.get(pk=id)

                votes = story.votes
                self.object = form.save(commit=False)
                self.object.votes = votes + 1
                self.object = form.save()
                messages.success(self.request, "You have {0} votes left".format(num_votes))
            else: 
                messages.error(self.request, "You don't have enough votes for this transaction.")
        except ValueError:
            messages.error(self.request, "You don't have enough votes for this transaction.")
            return redirect('payments:plans')

        return redirect('user:dashboard')


class StoryDownVoteView(LoginRequiredMixin, UpdateView):
    model = Story
    form_class = DownVoteForm

    def form_valid(self, form):
        id = self.object.id
        story = Story.objects.get(pk=id)
        votes = story.votes
        self.object = form.save(commit=False)
        self.object.votes = votes - 1
        self.object = form.save()
        return redirect('user:dashboard') 


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'content', 'genre']
    template_name = 'story/create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect('user:dashboard')


class StoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Story
    fields = ['title', 'content', 'genre']
    template_name = 'story/update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect('user:dashboard')


class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Story
    template_name = 'story/delete.html'
