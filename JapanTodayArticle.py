import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import ArticleToPdf as atp
import gzip

class Article:
    """
    Class of an Japan Today's article
    """
    def __init__(self):
        pass

    def setUrl(self, url_in):
        """
        Set a url for one article
        """
        self.url = url_in

    def fetch(self):
        """
        fetch html data and parse title and content
        """
        headers = {'Accept-Encoding': 'gzip'}
        request = urllib.request.Request(url=self.url, headers=headers)

        with urllib.request.urlopen(request) as response:
            html = response.read()

        # Decompress gzip-fetched html
        html = gzip.decompress(html)

        # Decode to utf-8. Exceptions will be replaced
        html = html.decode('utf-8','replace')

        # Parse it to elements
        soup = BeautifulSoup(html, "html.parser")

        # Get title and content of article
        # self.title = soup.find("h1", {"itemprop":"headline"}).get_text()
        self.title = soup.find("h1").get_text()
        print(self.title)
        self.article = soup.find("div", {"itemprop":"articleBody"}).get_text()

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.article

    def save(self):
        return atp.saveAsPdf(self.title, self.article)
