from datetime import timedelta

import pytest
import responses
from requests import Timeout
from requests import RequestException

from domainCheck.crawlers.domain import DomainCrawler


@responses.activate
def test_response_time_feature():
    dc = DomainCrawler()
    base_url = 'http://presslabs.com'
    responses.add(responses.GET, base_url, status=200)
    dc.crawl(base_url)
    res_list_tuples = dc.get_results_list()
    assert len(res_list_tuples) == len(dc.FEATURES_LIST)
    assert res_list_tuples[0][0].get_value()['value'] <= 0.1


@responses.activate
def test_response_time_feature_timeout():
    with pytest.raises(RequestException):
        dc = DomainCrawler()
        base_url = 'http://presslabs.com'

        def request_callback(request):
            raise Timeout()

        responses.add_callback(
            responses.GET, base_url,
            callback=request_callback
        )

        dc.crawl(base_url)
        res_list = dc.get_results_list()
        assert res_list == []


@responses.activate
def test_response_time_404():
    with pytest.raises(RequestException):
        dc = DomainCrawler()
        base_url = 'http://presslabs.com'
        responses.add(responses.GET, base_url, status=404)
        dc.crawl(base_url)
        res_list = dc.get_results_list()
        assert res_list == []
