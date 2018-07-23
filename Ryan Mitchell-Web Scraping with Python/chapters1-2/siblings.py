"""
The BeautifulSoup next_siblings() function makes it trivial to collect data from tables, especially ones with title rows
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_obj = BeautifulSoup(html, "html.parser")

siblings = soup_obj.find('table', {"id": "giftList"}).tr.next_siblings

for sibling in siblings:
    print(sibling)