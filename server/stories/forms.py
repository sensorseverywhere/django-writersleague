from django import forms

from .models import Story


class StoryCreateForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'content', 'genre', 'live')


class UpVoteForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('votes',)


class DownVoteForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('votes',)
