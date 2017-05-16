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
    def get_base_value():
        pass


class ValueObject:

    feature_name = "response_time"

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value
