import logging


from domainCheck.features.base import BaseFeature
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class HasCDNFeature(BaseFeature):

    def run(self, response):
        url = response.url
        soup = BeautifulSoup(response.content, 'html.parser')
        items_with_href = soup.find_all(href=True)
        hrefs = [item.get('href') for item in items_with_href]
        hrefs_with_cdn = [item for item in hrefs if 'cdn' in item]
        if len(hrefs_with_cdn) >= len(hrefs)/2:
            self.value = True
            return
        domain = extract_domain(url)
        imgs = soup.find_all('img')
        img_srcs = [item.get('src') for item in imgs]
        imgs_with_cdn = [item for item in img_srcs if domain in item]
        if len(imgs_with_cdn) >= len(imgs) * 0.8:
            self.value = True
            return
        self.value = False

    def extract_domain(url):
        dot_indexes = [i for i, chr in enumerate(url) if chr == '.']
        if len(dot_indexes) > 1:
            return url[(dot_indexes[-2]+1):]
        return url

    def get_result(self):
        return ValueResult(self.value)

    @staticmethod
    def get_compare_value():
        return ValueObject(True)

    @staticmethod
    def get_static_url(self, url):
        pass
