from abc import ABCMeta


class BaseFeature(metaclass=ABCMeta):

    @abstractmethod
    def run(self, base_url):
        raise NotImplementedError("This method should be overridden")

    @staticmethod
    def get_compare_value():
        raise NotImplementedError("This method should be overridden")
