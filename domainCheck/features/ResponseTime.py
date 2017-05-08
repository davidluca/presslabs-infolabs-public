import requests


from domainCheck.features.base import BaseFeature


class ResponseTimeFeature(BaseFeature):

    TYPE = 'value'

    def run(self, base_url):
        resp = requests.get(base_url)
        return {
            'value': resp.elapsed
        }

    @staticmethod
    def get_compare_value():
        return {
            'value': 100
        }
