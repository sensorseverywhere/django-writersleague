from rest_framework import serializers

from .models import Story
from user.serializers import CustomUserSerializer


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = '__all__'
        
