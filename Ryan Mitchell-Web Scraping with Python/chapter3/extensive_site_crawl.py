"""
The general approach to an exhaustive site crawl is to start with a top-level page (such as the home page), and search
for a list of all internal links on that page. Every one of those links is then crawled, and additional lists of links
are found on each one of them, triggering another round of crawling.

WARNING:  if left running long enough, this program will almost certainly crash.
Python has a default recursion limit (how many times programs can recursively call themselves) of 1,000.
Because Wikipedia’s net‐ work of links is extremely large, this program will eventually hit that recursion limit and
stop, unless you put in a recursion counter or something to prevent that from happening.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()


def get_links(page_url):
    global pages
    html = urlopen('http://en.wikipedia.org' + page_url)
    soup_obj = BeautifulSoup(html, 'html.parser')

    try:
        print(soup_obj.h1.get_text())
        print(soup_obj.find(id ="mw-content-text").findAll('p')[0])
        print(soup_obj.find(id="ca-edit").find('span').find('a').attrs['href'])
    except AttributeError:
        print('Page is missing')

    links = soup_obj.findAll('a', href=re.compile('^(/wiki/)'))
    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                new_page = link.attrs['href']
                print("----------------\n"+new_page)
                pages.add(new_page)
                get_links(new_page)

if __name__ == '__main__':
    get_links("")  # start from index page
