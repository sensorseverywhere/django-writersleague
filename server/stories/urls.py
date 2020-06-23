from django.urls import path

from .views import StoryCreateView, StoryDetailView, StoryListView, StoryCreateAPIView, StoryListAPIView, StoryDetailAPIView

app_name = 'story'

urlpatterns = [
    path('', StoryListView.as_view(), name="story_list"),
    path('story/create/', StoryCreateView.as_view(), name="story_create"),
    path('story/<int:pk>/', StoryDetailView.as_view(), name="story_detail"),

    path('api/stories/', StoryListAPIView.as_view(), name="api_story_list"),
    path('api/story/<int:pk>/', StoryDetailAPIView.as_view(), name="api_story_detail"),
    path('api/story/create/', StoryCreateAPIView.as_view(), name="api_story_create"),
]