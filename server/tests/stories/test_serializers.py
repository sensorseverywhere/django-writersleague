import pytest

from user.models import CustomUser
from stories.serializers import StorySerializer


@pytest.mark.django_db
def test_valid_story_serializer():
    print("PRINT")
    user = CustomUser.objects.create_user(
        "test@test.com",
    )

    user = CustomUser.objects.all()
    print(user)
    print('alsdkjflaskdjf')
    # valid_serializer_data = {
    #     'title': "World's Greatest...",
    #     'content': "Story Content",
    #     'author': user_pk,
    #     'status': 0,
    #     'genre': 1,
    #     'votes': 34,
    #     'live': True
    # }
    # serializer = StorySerializer(data=valid_serializer_data)
    # assert serializer.is_valid()
    # assert serializer.validated_data == valid_serializer_data
    # assert serialzer.data == valid_serializer_data
    # assert serializer.errors == {}

def test_invalid_story_serializer():
    invalid_serializer_data = {
        'title': 'Worlds Greatest...',
        'content': 'Some Content'
    }
    serializer = StorySerializer(data=invalid_serializer_data)
    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    print(serializer.errors)