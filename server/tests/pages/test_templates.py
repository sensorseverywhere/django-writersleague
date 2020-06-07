from django.test import TestCase


def test_home_page_works(TestCase):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/home.html')
    self.assertContains('Home')