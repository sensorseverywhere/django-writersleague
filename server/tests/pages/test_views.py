import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_home_page_view(client):
    url = reverse('pages:home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_page_detail_view_context_data(client, **kwargs):
    url = reverse('pages:about')
    res = client.get(url)
    assert len(res.context['contents']) == 0
