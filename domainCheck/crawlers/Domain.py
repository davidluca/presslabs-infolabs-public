import requests


from domainCheck.crawlers.base import BaseCrawler
from domainCheck.features.ResponseTime import ResponseTimeFeature


class DomainCrawler(BaseCrawler):

    FEATURE_LIST = [ResponseTimeFeature]

    def crawl(self, base_url):
        response = requests.get(base_url)
        for feature_class in FEATURES_LIST:
            feature_instance = feature_class()
            feature_instance.run()
            result = feature_instance.get_result()
            results_list.append(result)
