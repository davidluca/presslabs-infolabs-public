from abc import ABCMeta, abstractmethod


class BaseFeature(metaclass=ABCMeta):

    def __init__(self):
        self.value = None

    @abstractmethod
    def run(self, response):
        pass

    @abstractmethod
    def get_result(self):
        pass

    @staticmethod
    @abstractmethod
    def get_compare_value():
        pass

    @staticmethod
    @abstractmethod
    def get_static_url(self, url):
        pass
