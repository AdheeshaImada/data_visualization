import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

print("..........................................................................................................")

results = []

# Create a Selenium WebDriver instance (e.g., for Chrome)
driver = webdriver.Chrome()

def get_title(title_url):
    try:
        # Use Selenium to navigate to the URL
        driver.get(title_url)
        #time.sleep(60)  # Pause for 60 seconds

    except HTTPError as e:
        return e
    except URLError as e:
        return "This server could not be found, %s" % e

    # Use BeautifulSoup to parse the page source
    bs = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        content = bs.find_all('ul', {'class': 'res_allnumber'})
        return content
    except AttributeError as e:
        return "%s, title not found" % e

url = "https://www.dlb.lk/result/en"

title = get_title(url)
for tl in title:
    print(tl)
    print("...........................................................................................................")

# Close the Selenium WebDriver when done
driver.quit()

print("Web scraping finished successfully")
