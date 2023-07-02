import requests
from bs4 import BeautifulSoup

from model.stock_real_time_price import StockInTheRealTimeModel

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
url = 'https://uk.finance.yahoo.com/quote/'


def get_stock_data(symbol) -> StockInTheRealTimeModel:
    request = requests.get(url + symbol, headers=headers)
    soup = BeautifulSoup(request.text, 'html.parser')

    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

    #find all find-streamer tag with class Fw(500) Pstart(8px) Fz(24px) and get the text of all of them and store in a list called changes
    changes = soup.find_all('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'})      #returns a list of all the tags with the specified class

    return StockInTheRealTimeModel(symbol= symbol, name ="")