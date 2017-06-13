import os

import pytest
from rest_framework.test import APIClient
from django_dynamic_fixture import G
from django.contrib.auth import get_user_model


@pytest.fixture
@pytest.mark.django_db
def api_client():
    user = G(get_user_model())  # create a user
    client = APIClient(format='json')
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def html_content():
    def html_content_wrapper(file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'r') as file:
            return file.read()
    return html_content_wrapper
