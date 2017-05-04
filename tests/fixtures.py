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

