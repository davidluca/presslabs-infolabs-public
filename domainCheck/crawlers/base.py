from abc import ABCMeta


class BaseCrawler(metaclass=ABCMeta):

    FEATURES_LIST = []
    results_list = []

    @abstractmethod
    def crawl(self):
        pass

    def get_results_list(self):
        return results_list
