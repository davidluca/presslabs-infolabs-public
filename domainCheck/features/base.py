from abc import ABCMeta


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

    def __init__(self, value):
        pass
