from domainCheck.features.base import BaseFeature, ValueResult


class ResponseTimeFeature(BaseFeature):

    def run(self, response):
        self.value = response.elapsed

    def get_result(self):
        return ValueResult(self.value)

    @staticmethod
    def get_base_value():
        return ValueResult(100)
