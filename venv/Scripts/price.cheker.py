import telebot
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot("1574024760:AAE4U1DKTLWHzCynuahPm_apI7l9CrGgUrE")

def parse():
    URL = 'https://www.avito.ru/rossiya/avtomobili'
    HEADERS = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }

    response = requests.get(URL, headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_ = 'offer-wrapper')
    comps = []

    for item in  items:
        comps.append({
            'title':item.find(a, class_ = "link-link-39EVK link-design-default-2sPEv title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc").get_text(strip = True)
        })
        for comp in comps:
            print(comp['title'])


parse()

bot.polling()