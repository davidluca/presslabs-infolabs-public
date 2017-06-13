import requests
import logging

from domainCheck.crawlers.base import BaseCrawler
from domainCheck.features.response_time import ResponseTimeFeature
from requests import RequestException

logger = logging.getLogger(__name__)


class DomainCrawler(BaseCrawler):

    FEATURES_LIST = [ResponseTimeFeature]

    def crawl(self, base_url):
        try:
            response = requests.get(base_url)
            response.raise_for_status()
            for feature_class in self.FEATURES_LIST:
                feature_instance = feature_class()
                feature_instance.run(response)
                result = feature_instance.get_result()
                compare_value = feature_instance.get_compare_value()
                self.results_list.append((result,
                                          feature_class.__name__,
                                          compare_value))
        except RequestException as re:
            logger.exception(RequestException)
            raise
