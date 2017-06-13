import os

import pytest
import responses
import requests

from domainCheck.features.has_cdn import HasCDNFeature
from tests.fixtures import html_content


@responses.activate
def test_hasCDN_feature_success(html_content):
    hasCDN_instance = HasCDNFeature()
    base_url = 'http://www.presslabs.com'
    responses.add(responses.GET,
                  base_url,
                  body=html_content('features/html_file_with_cdn.html'),
                  status=200)
    response = requests.get(base_url)
    hasCDN_instance.run(response)
    assert hasCDN_instance.get_result().get_value()['value'] is True
