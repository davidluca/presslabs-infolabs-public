from domainCheck.features.base import BaseFeature
from domainCheck.value_result import ValueResult


class ResponseTimeFeature(BaseFeature):

    def run(self, response):
        self.value = response.elapsed

    def get_result(self):
        return ValueResult(self.value.total_seconds())

    @staticmethod
    def get_compare_value():
        return ValueResult(100)

    @staticmethod
    def get_static_url(self, url):
        pass
