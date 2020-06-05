import pytest


def test_home_page_works(client):
    response = client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/home.html')
    self.assertContains('Home')