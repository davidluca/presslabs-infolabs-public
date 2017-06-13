import logging
from urllib.parse import urlparse

from publicsuffix import fetch, PublicSuffixList
from bs4 import BeautifulSoup

from domainCheck.features.base import BaseFeature
from domainCheck.value_result import ValueResult

logger = logging.getLogger(__name__)


class HasCDNFeature(BaseFeature):

    def run(self, response):
        url = response.url
        psl_file = fetch()
        psl = PublicSuffixList(psl_file)
        domain = psl.get_public_suffix(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        items_with_href = soup.find_all(href=True)
        hrefs = [item.get('href') for item in items_with_href]
        imgs = soup.find_all('img')
        img_srcs = [item.get('src') for item in imgs]
        links = img_srcs + hrefs
        self.value = self.has_cdn(domain, links)

    def has_cdn(self, domain, links):
        return self.cdn_in_url(links) or self.subdomain_cdn(domain, links)

    def cdn_in_url(self, links):
        links_with_cdn = [link for link in links if 'cdn' in link]
        if len(links_with_cdn) >= len(links)/2:
            return True
        return False

    def subdomain_cdn(self, domain, links):
        urls_netloc = [urlparse(link).netloc for link in links]
        subdomains = [netloc for netloc in urls_netloc if domain in netloc]
        if len(subdomains) >= len(links) * 0.8:
            return True
        return False

    def get_result(self):
        return ValueResult(self.value)

    @staticmethod
    def get_compare_value():
        return ValueObject(True)

    @staticmethod
    def get_static_url(self, url):
        pass
