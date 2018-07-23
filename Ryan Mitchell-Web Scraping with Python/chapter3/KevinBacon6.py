"""
In this section, we’ll begin a project that will become a “Six Degrees of Wikipedia" solution finder. That is, we’ll
be able to take the Eric Idle page and find the fewest num‐ ber of link clicks that will take us to the Kevin Bacon
page.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
soup_obj = BeautifulSoup(html, 'html.parser')
links = soup_obj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))

for link in links:
    if 'href' in link.attrs:
        print(link.attrs['href'])

