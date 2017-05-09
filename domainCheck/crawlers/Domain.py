import requests


from domainCheck.crawlers.base import BaseCrawler
from domainCheck.features.ResponseTime import ResponseTimeFeature


class DomainCrawler(BaseCrawler):

    FEATURES_LIST = [ResponseTimeFeature]

    def crawl(self, base_url):
        response = requests.get(base_url)
        for feature_class in self.FEATURES_LIST:
            feature_instance = feature_class()
            feature_instance.run(response)
            result = feature_instance.get_result()
            self.results_list.append(result)
