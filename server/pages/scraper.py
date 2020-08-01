import json
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

start_link = 'https://www.commercialrealestate.com.au/news/'
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(start_link, headers=hdr)
start_page = urlopen(req)
soup = BeautifulSoup(start_page, 'html.parser')
news_links = []
news_title = []
news_content = []
news_image = []

curr_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(curr_dir, 'fixtures/news.json')


for link in soup.find_all('a', attrs={'class': 'tile-domain-news__media-link'}):
    news_links.append(link.get('href'))

for thumb_image in soup.find_all('img', attrs={'class': 'tile-domain-news__media'}):
    news_image.append(thumb_image.get('src'))

news_links = news_links[:3]
news_image = news_image[:3]

for index, link in enumerate(news_links):
    req_news_page = Request(link, headers=hdr)
    news_page = urlopen(req_news_page)
    ns = BeautifulSoup(news_page, 'html.parser')

    for title in ns.find('h1', attrs={'class': 'domain-article-title'}):
        news_title.append(title)

    for content in ns.find_all('p', attrs={'class': 'first-para'}):
        news_content.append(content.get_text())
        print(content.get_text())

    data = [
        {
            'model': 'pages.newsitem',
            'fields': {
                'url': news_links[index],
                'title': news_title[index],
                'content': news_content[index],
                'image_url': news_image[index],
                'active': False,
                'date_added': '2019-10-23T18:30:49.797Z',
                'date_updated': '2019-10-23T18:30:49.797Z'
            }
        }
    ]

    with open(file_path, 'a', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
