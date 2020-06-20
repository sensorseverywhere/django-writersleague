# from django.test import TestCase
# from ..models import CustomUser


# class TestCustomUserModel(TestCase):

#     def test_saving_and_retrieving_users(self):
#         password = 'Qqqqqq!1'

#         first_user = CustomUser({
#             'email': "user2@test.com",
#             'user_type': 0,
#             'password': password,
#             'password2': password
#         })
#         first_user.save()
#         second_user = CustomUser({
#             'id': 2,
#             'email': "user2@test.com",
#             'user_type': 1,
#             'password': password,
#             'password2': password
#         })
#         second_user.save()

#         saved_users = CustomUser.objects.all()
#         self.assertEqual(saved_users.count(), 2)

