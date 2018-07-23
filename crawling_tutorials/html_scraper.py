from bs4 import BeautifulSoup
import csv
import requests


url = 'http://coreyms.com'

source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")

csv_file = open('coreyms.com.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'link'])

for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print('Headline:\n', headline)

    summary = article.find('div', class_='entry-content').p.text
    print('Summary:\n', summary)

    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        video_id = video_src.split('/')[4].split('?')[0]
        youtube_link = 'https://youtube.com/watch?v={}'.format(video_id)
    except Exception as e:
        youtube_link = None

    print('Link:\n', youtube_link)
    csv_writer.writerow([headline, summary, youtube_link])

csv_file.close()

