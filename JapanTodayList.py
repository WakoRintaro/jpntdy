import xml.etree.ElementTree as ET
import urllib.request
import send_mail as sm
from JapanTodayArticle import Article

# Number of fetched feeds
NUM_FEED = 5

# Japan Today's feed url
URL_FEED = "https://japantoday.com/feed"

if __name__ == '__main__':
    # Fetch XML data
    with urllib.request.urlopen(URL_FEED) as response:
       html = response.read()
    # parser
    root = ET.fromstring(html)

    # attachment list
    attachment_list = []
    i = 0
    for link in root.iter('link'):
        print("[" + str(i) + "]" + link.text)
        if i >= 1 and i<= NUM_FEED:
            # article[0] is a link to its root page
            article = Article()
            article.setUrl(link.text)
            article.fetch()
            attachment_list.append(article.save())
            del article
        i+=1

    # Send PDF articles by email
    msg = sm.create_message(attachment_list)
    sm.send(msg)
