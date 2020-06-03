# from django.http import HttpRequest
# from django.urls import resolve, reverse
# from django.core import mail 
# from django.test import RequestFactory, TestCase

# from pages import forms
# from .views import HomePageView

# class HomePageViewTest(TestCase):

#     def test_root_url_resolves_to_homepage_view(self):
#         request = RequestFactory().get('/')
#         view = HomePageView()
#         view.setup(request)

#     def test_home_page_returns_correct_html(self):
#         response = self.client.get(reverse('home'))
#         html = response.content.decode('utf8')  
#         self.assertTrue(html.startswith('<!doctype html>'))
#         self.assertIn('<title>Plotify | This is a title</title>', html)      


# class TestForm(TestCase):
#     def test_valid_contact_form_sends_email(self):
#         form = forms.ContactForm({
#             'name': 'Luke Skywalker',
#             'email': 'luke@thedeathstar.com',
#             'phone': '008234234',
#             'message': 'Enquiry for Plotify'
#         })
#         self.assertTrue(form.is_valid())

#         form.send_mail()
        
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertEqual(mail.outbox[0].subject, 'Enquiry for Plotify')


#     def test_invalid_contact_form(self):
#         form = forms.ContactForm({
#             'message': "yo"
#         })
#         self.assertFalse(form.is_valid())


    