from domainCheck.features.base import BaseFeature, ValueObject


class ResponseTimeFeature(BaseFeature):

    def run(self, response):
        response.raise_for_status()
        self.value = response.elapsed


    def get_result(self):
        return ValueObject(self.value)

    @staticmethod
    def get_base_value():
        return ValueObject(100)
