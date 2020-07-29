import json
import re
import pytest
from user.models import CustomUser





@pytest.mark.django_db
def test_user_model_create(client):
    user = CustomUser.objects.create_user(
        "test@test.com",
        "password1"
    )
    assert CustomUser.objects.count() == 1


# def check_email_format(email):
#     """check that the entered email format is correct"""
#     if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
#         raise Exception("Invalid email format")
#     else:
#         return "Email format is ok"

# def test_email_exception():
#     """test that exception is raised for invalid emails"""
#     user = CustomUser.objects.create_user(
#         "",
#     )
#     with pytest.raises(Exception):
#         assert check_email_format("")
