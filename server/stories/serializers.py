from rest_framework import serializers
from .models import Story
from account.serializers import CustomUserSerializer



class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['title', 'content', 'genre', 'author']
        
