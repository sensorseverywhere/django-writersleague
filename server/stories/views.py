
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from rest_framework import generics

from .forms import UpVoteForm, DownVoteForm
from .models import Story, UserStoryVotes
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
            user_story_votes = UserStoryVotes.objects.filter(voter=self.request.user, story=self.object)
            context['num_votes'] = user.num_votes
            context['votes'] = user_story_votes.count()
        context['upvote_form'] = UpVoteForm()
        context['downvote_form'] = DownVoteForm()

        return context


class StoryUpVoteView(LoginRequiredMixin, UpdateView):
    model = Story
    form_class = UpVoteForm
    # template_name = 'story/upvote.html'

    def form_valid(self, form):
        id = self.object.id
        user = CustomUser.objects.get(pk=self.request.user.id)
        # count user story vote
        user_story_votes = UserStoryVotes.objects.create(voter=user, story=self.object, votes=1)
        num_votes = user.num_votes
        try:
            if num_votes >= 1:
                num_votes = num_votes - 1
                user.num_votes = num_votes
                user.save()
                story = Story.objects.get(pk=id)

                votes = story.votes
                self.object = form.save(commit=False)
                self.object.votes = votes + 1
                self.object = form.save()

                messages.success(self.request, "You have {0} votes left".format(num_votes))

            else:
                messages.error(
                    self.request,
                    "You don't have enough votes for this transaction. If you like, you can purchase more below.")
                return redirect('products:plans')
        except ValueError:
            messages.error(
                self.request,
                "You don't have enough votes for this transaction.")
            return redirect('products:plans')
        if user.user_type == 1:
            return redirect('user:dashboard')
        else:
            return redirect('story:story_detail', pk=self.object.id)


class StoryDownVoteView(LoginRequiredMixin, UpdateView):
    model = Story
    form_class = DownVoteForm

    def form_valid(self, form):
        user = CustomUser.objects.get(pk=self.request.user.id)
        user_story_votes = UserStoryVotes.objects.filter(voter=self.request.user, story=self.object)
        votes_user_has = user_story_votes.count()
        num_votes = user.num_votes
        try:
            if votes_user_has > 0:
                # remove one user_story_votes record
                UserStoryVotes.objects.filter(voter=self.request.user, story=self.object).last().delete()

                num_votes = num_votes + 1
                user.num_votes = num_votes
                user.save()
                id = self.object.id
                story = Story.objects.get(pk=id)

                votes = story.votes
                self.object = form.save(commit=False)
                self.object.votes = votes - 1
                self.object = form.save()
                messages.success(self.request, "You have {0} votes left".format(num_votes))
            else:
                messages.error(self.request, "You have already removed all your votes from this story.")

        except ValueError:
            messages.error(self.request, "You don't have enough votes for this transaction.")
            return redirect('products:plans')

        if user.user_type == 1:
            return redirect('user:dashboard')
        else:
            return redirect('story:story_detail', pk=self.object.id)


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
