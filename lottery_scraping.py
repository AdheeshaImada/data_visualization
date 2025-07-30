import time
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

print("..........................................................................................................")

results = []


def gettitle(title_url):
    try:
        html = urlopen(title_url)
        time.sleep(60)
        print('ok')
    except HTTPError as e:
        return e
    except URLError as e:
        return "This server could not found, %s" % e
    bs = BeautifulSoup(html.read(), 'html.parser')
    try:
        content = bs.find_all('ul', {'class': 'res_allnumber'})
        return content
    except AttributeError as e:
        return "%s, title not found" % e


url = "https://www.dlb.lk/result/en"

title = gettitle(url)
for tl in title:
    print(tl)
    print("...........................................................................................................")
print("Web scraping finished successfully")
