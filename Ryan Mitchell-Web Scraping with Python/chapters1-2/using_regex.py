from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_obj = BeautifulSoup(html, "html.parser")

product_images = soup_obj.findAll("img", {"src": re.compile("\.\./img/gifts/img.*\.jpg")})

for image in product_images:
    print(image['src'])

# This prints out only the relative image paths that start with ../img/gifts/img and end in .jpg
