"""
If you want to find only descendants that are children, you can use the  .children tag:
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup_obj = BeautifulSoup(html, "html.parser")

# list  of  product  rows  in  the  giftList table.
gift_list_children = soup_obj.find('table', {"id": "giftList"}).children

for child in gift_list_children:
    print(child)

"""
this code prints out the list of product rows in the giftList table. If you were to write it using the descendants()
function instead of the children() function, about two dozen tags would be found within the table and printed, 
including img tags, span tags, and individual td tags. It’s definitely important to differentiate between children and 
descendants!
"""