class StockData:
    def __init__(self, symbol, currency, date_time,
                 timestamp, open, high, low, close, volume, created_at, symbol_id, type_profile, adj_close):
        self.symbol_id = symbol_id
        self.symbol = symbol
        self.currency = currency
        self.date_time = date_time
        self.timestamp = timestamp
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.created_at = created_at
        self.type_profile = type_profile
        self.adj_close = adj_close

    def __str__(self) -> str:
        return f"StockData(symbol={self.symbol}, currency={self.currency}, date_time={self.date_time}, " \
               f"timestamp={self.timestamp}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, " \
               f"volume={self.volume}, created_at={self.created_at}, type_profile={self.type_profile}" \

    def getTypeOfEachAttribute(self):
        return {
            "symbol": type(self.symbol),
            "currency": type(self.currency),
            "date_time": type(self.date_time),
            "timestamp": type(self.timestamp),
            "open": type(self.open),
            "high": type(self.high),
            "low": type(self.low),
            "close": type(self.close),
            "volume": type(self.volume),
            "created_at": type(self.created_at)
        }