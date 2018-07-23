from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html, "html.parser")

name_list = soup.findAll("span", {"class": "green"})
name_set = set()

for name in name_list:
    # .get_text() strips  all  tags  from  the  document  you  are  working with  and  returns  a  string  containing
    #  the  text  only.
    name_set.add(name.get_text())

for name in name_set:
    print(name)

