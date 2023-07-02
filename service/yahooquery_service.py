from typing import List

from pandas import DataFrame

from model.company_profile import CompanyProfile
from model.stockData import StockData
from yahooquery import Ticker
import datetime

from utils.StockDataType import StockDataType


def get_stock_data_by_yahoo_finance(symbol, model_profile: CompanyProfile) -> list[StockData]:
    # https://pypi.org/project/yahooquery/

    try:
        ticker = Ticker(symbol, asynchronous=True)
    except Exception as e:
        raise e

    list_of_stock_data = []

    currency = ticker.summary_detail[symbol]['currency']

    # get stock price data
    data = ticker.history(period="max")
    list_index_date = data.index.to_list()

    for item in list_index_date:
        _, date_index = item

        if isinstance(model_profile, CompanyProfile):
            data_row = data.loc[(symbol, date_index)]
            datetime_obj = datetime.datetime.combine(date_index, datetime.time())

            list_of_stock_data.append(StockData(symbol=symbol,
                                                open=data_row['open'],
                                                high=data_row['high'],
                                                low=data_row['low'],
                                                close=data_row['close'],
                                                volume=data_row['volume'],
                                                adj_close=data_row['adjclose'],
                                                currency=currency,
                                                created_at=int(datetime.datetime.now().timestamp() * 1000000),
                                                date_time=date_index,
                                                timestamp=int(datetime_obj.timestamp() * 1000),
                                                type_profile=StockDataType.COMPANY,
                                                symbol_id=model_profile.id))

    return list_of_stock_data


def get_company_profile_information(symbol) -> CompanyProfile:
    # https://pypi.org/project/yahooquery/

    try:
        ticker = Ticker(symbol, asynchronous=True)
    except Exception as e:
        raise e

        # get company profile information
    company_information = ticker.summary_profile[symbol]

    return CompanyProfile(symbol=symbol,
                          address=company_information['address1'],
                          city=company_information['city'],
                          state=company_information['state'] if 'state' in company_information else None,
                          zip=company_information['zip'],
                          country=company_information['country'],
                          website=company_information['website'],
                          sector=company_information['sector'],
                          industry=company_information['industry'])
