from django import forms

from .models import Story


class StoryCreateForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'content', 'genre')