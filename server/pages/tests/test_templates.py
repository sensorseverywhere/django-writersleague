from django.test import TestCase


class TestPage(TestCase):
    def test_home_page_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'Home')

    def test_about_page_location(self):
        response = self.client.get('/#about-wl')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertContains(response, 'About')