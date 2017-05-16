from abc import ABCMeta, abstractmethod


class BaseCrawler(metaclass=ABCMeta):

    FEATURES_LIST = []

    def __init__(self):
        self.results_list = []

    @abstractmethod
    def crawl(self):
        pass

    def get_results_list(self):
        return self.results_list
