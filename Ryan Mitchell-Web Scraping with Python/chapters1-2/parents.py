"""
Occasionally, however, you can find yourself in odd situations that require BeautifulSoup’s parent-finding functions,
.parent and .parents . For example:
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_obj = BeautifulSoup(html, "html.parser")

parent_of_img = soup_obj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text()

print(parent_of_img)
