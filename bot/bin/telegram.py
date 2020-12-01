from bs4 import BeautifulSoup
from requests import get

# simple code that retrieve ip from telegram public channel via scraping

page = get(url = 'https://t.me/s/q23rty')
soup = BeautifulSoup(page.content, features = 'html.parser')
messages = soup.findAll('div', attrs = {'class' : 'tgme_widget_message_text'})
ip = messages[-1].find('a').text
print(ip)
