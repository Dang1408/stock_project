import uuid

from model.stockData import StockData


class Stockdatadao:
    def __init__(self, db):
        self.db = db

    def insert(self, model: StockData):
        cur = self.db.cursor()
        sql = """INSERT INTO stock_data(symbol_id, symbol, currency, date_time, timestamp, 
                                                    open, high, low, close, volume, created_at, type_profile,adj_close) """ \
              """VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s)"""
        val = (model.symbol_id, model.symbol, model.currency,
               model.date_time, model.timestamp, model.open, model.high, model.low, model.close,
               model.volume, model.created_at, model.type_profile.value, model.adj_close)
        cur.execute(sql, val)
        self.db.commit()

    def select(self, symbol):
        cursor = self.db.cursor()
        sql = """SELECT date_time, open, high, low, close, volume, adj_close 
                    FROM stock_data WHERE symbol = %s"""
        val = (symbol,)

        cursor.execute(sql, val)
        result = cursor.fetchall()
        list_stock_data = []

        for item in result:
            list_stock_data.append(
                StockDataViewModel(date_time=item[0], open=item[1], high=item[2], low=item[3],
                                   close=item[4], volume=item[5], adj_close=item[6]))

        cursor.close()
        if result is None:
            return None
        else:
            return list_stock_data


class StockDataViewModel:
    def __init__(self, date_time, open, high, low, close, volume, adj_close):
        self.date_time = date_time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.adj_close = adj_close
