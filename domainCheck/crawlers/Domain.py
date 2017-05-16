import requests
import logging

from domainCheck.crawlers.base import BaseCrawler
from domainCheck.features.ResponseTime import ResponseTimeFeature
from requests import RequestException

logger = logging.getLogger(__name__)

class DomainCrawler(BaseCrawler):

    FEATURES_LIST = [ResponseTimeFeature]

    def crawl(self, base_url):
        logger.exception("----------" + base_url)
        # print("asdasdsadsad " + base_url)
        try:
            response = requests.get(base_url)
            for feature_class in self.FEATURES_LIST:
                feature_instance = feature_class()
                feature_instance.run(response)
                result = feature_instance.get_result()
                self.results_list.append(result)
        except RequestException as re:
            logger.exception(RequestException)

