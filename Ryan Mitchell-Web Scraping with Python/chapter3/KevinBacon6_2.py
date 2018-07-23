"""
A Program that contains:

- A single function, getLinks , that takes in a Wikipedia article URL of the form / wiki/<Article_Name> and returns a
list of all linked article URLs in the same form.

- A main function that calls getLinks with some starting article, chooses a random article link from the returned list,
and calls getLinks again, until we stop the program or until there are no article links found on the new page.

WARNING:  if left running long enough, this program will almost certainly crash.
Python has a default recursion limit (how many times programs can recursively call themselves) of 1,000.
Because Wikipedia’s net‐ work of links is extremely large, this program will eventually hit that recursion limit and
stop, unless you put in a recursion counter or something to prevent that from happening.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen('http://en.wikipedia.org' + article_url)
    soup_obj = BeautifulSoup(html, 'html.parser')
    links = soup_obj.find("div", {'id': 'bodyContent'}).findAll("a", href=re.compile('^(/wiki/)((?!:).)*$'))
    return links


def main():
    links = get_links('/wiki/Kevin_Bacon')
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs['href']
        print(new_article)
        links = get_links(new_article)


if __name__ == '__main__':
    main()
