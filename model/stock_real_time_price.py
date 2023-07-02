class StockInTheRealTimeModel:
    def __init__(self, symbol, name, currency, date_time, timestamp, price, change, change_percent, created_at):
        self.symbol = symbol
        self.name = name
        self.currency = currency
        self.date_time = date_time
        self.timestamp = timestamp
        self.price = price
        self.change = change
        self.change_percent = change_percent
        self.created_at = created_at

    def __str__(self) -> str:
        return f"Stock(symbol={self.symbol}, name={self.name}, " \
               f"currency={self.currency}, date_time={self.date_time}, " \
               f"timestamp={self.timestamp}, price={self.price}, " \
               f"change={self.change}, change_percent={self.change_percent}, created_at={self.created_at})"
