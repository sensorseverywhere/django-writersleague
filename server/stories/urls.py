from django.urls import path

from .views import StoryCreateView, StoryDetailView, StoryListView

app_name = 'story'

urlpatterns = [
    path('', StoryListView.as_view(), name="story_list"),
    path('story/create/', StoryCreateView.as_view(), name="story_create"),
    path('story/<int:pk>/', StoryDetailView.as_view(), name="story_detail"),