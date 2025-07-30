from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs

url = "https://www.dlb.lk/result/en"

html = urlopen(url)

bs = Bs(html.read(), "html.parser")

contents = bs.find('div', {'class': "col-lg-9 col-md-12 col-sm-12 col-xs-12 tab-content"}).find('div', {'class': 'col-lg-7'}).find_all("h6")

numbers, letters = [], []
for index, content in enumerate(contents):
    if index == 0 or ((index+1) % 6) == 0:
        letters.append(content.get_text())
    else:
        numbers.append(content.get_text())
    print("*********************************************************************")

print(numbers)
print(letters)
