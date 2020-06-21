import json

import pytest
from account.models import CustomUser
from stories.models import Story


@pytest.mark.django_db
def test_story_model(client):
    user = CustomUser.objects.create_user(
        "test@test.com",
    )

    story = Story(
        title="World's Greatest...",
        content="Story Content",
        author=user,
        status=0,
        genre=1,
        votes=34,
        live=True
    )
    story.save()
    assert story.title == "World's Greatest..."
    assert story.content == "Story Content"
    assert story.votes == 34
    assert str(story) == story.title