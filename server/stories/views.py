
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView

from rest_framework import generics

from .models import Story
from .serializers import StorySerializer


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
