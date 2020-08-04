# import pytest

# from django.urls import reverse


# @pytest.mark.django_db
# def test_story_list_view(client):
#    url = reverse('story:story_list')
#    response = client.get(url)
#    assert response.status_code == 200


# @pytest.mark.django_db
# def test_unauthorized_story_create_view(client):
#    url = reverse('story:story_create')
#    response = client.get(url)
#    assert response.status_code == 302
