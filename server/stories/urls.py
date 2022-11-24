from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path(
        'stories/',
        views.StoryListView.as_view(),
        name="story_list"
        ),
    path(
        'story/<int:pk>/',
        views.StoryDetailView.as_view(),
        name="story_detail"
        ),
    path(
        'story/<int:pk>/upvote/',
        views.StoryUpVoteView.as_view(),
        name="story_upvote"
    ),
    path(
        'story/<int:pk>/downvote/',
        views.StoryDownVoteView.as_view(),
        name="story_downvote"
    ),
    path(
        'story/create/',
        views.StoryCreateView.as_view(),
        name="story_create"
        ),
    path(
        'story/update/<int:pk>/',
        views.StoryUpdateView.as_view(),
        name="story_update"
        ),
    path(
        'story/delete/<int:pk>/',
        views.StoryDeleteView.as_view(),
        name="story_delete"
        ),

    path(
        'api/stories/',
        views.StoryListAPIView.as_view(),
        name="api_story_list"
        ),
    path(
        'api/story/<int:pk>/',
        views.StoryDetailAPIView.as_view(),
        name="api_story_detail"
        ),
    path(
        'api/story/create/',
        views.StoryCreateAPIView.as_view(),
        name="api_story_create"
        ),
    path(
        'api/story/update/<int:pk>/',
        views.StoryUpdateAPIView.as_view(),
        name="api_story_update"
        ),
]
