from numpy import longlong
from model.stockData import StockData as stockInTheEndOfDay
from twelvedata import TDClient
import datetime


def get_stock_price_data_of_symbol(symbol) -> stockInTheEndOfDay:
    # Initialize client - apikey parameter is requiered
    td = TDClient(apikey="101acd35ff6c4d22810014c3060648f8")

    quote = td.quote(
        symbol=symbol,
        exchange="NASDAQ",
        type="stock"
    )

    temp = quote.as_json()
    return stockInTheEndOfDay(symbol=symbol,
                              name=temp['name'],
                              exchange=temp['exchange'],
                              mic_code=temp['mic_code'],
                              currency=temp['currency'],
                              date_time=temp['datetime'],
                              timestamp=temp['timestamp'],
                              open=temp['open'],
                              high=temp['high'],
                              low=temp['low'],
                              close=temp['close'],
                              volume=temp['volume'],
                              created_at=int(datetime.datetime.now().timestamp() * 1000000))
