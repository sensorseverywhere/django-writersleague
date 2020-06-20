# import pytest
# from django.core import mail
# from django.shortcuts import reverse
# from account.forms import UserRegistrationForm


# @pytest.mark.django_db
# class TestForm():
#     def test_valid_registration_form_sends_email(self):
#         password = "Qqqqqq!1"

#         form = UserRegistrationForm(data={
#             'email': "test@user.com",
#             'user_type': 0,
#             'password': password,
#             'password2': password
#         })
        
#         self.assertTrue(form.is_valid())
        
#         with self.assertLogs('account.forms', level='INFO') as user_reg:
#             form.send_mail()
        
#         self.assertEqual(len(mail.outbox), 1)
#         self.assertEqual(mail.outbox[0].subject, 'Welcome to the Writers League!')
#         self.assertGreaterEqual(len(user_reg.output), 1)
    
#     def test_invalid_registration_form(self):
#         form = UserRegistrationForm({
#             'email': 'email@me.com'
#         })
#         self.assertFalse(form.is_valid())
    
#     def test_can_save_new_user(self):
#         password = "Qqqqqq!1"
#         res = self.client.post('register', data={
#                                                 'email': "test@user.com",
#                                                 'user_type': 0,
#                                                 'password': password,
#                                                 'password2': password
#                                             })