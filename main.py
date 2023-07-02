from dao.postgresql.company_profile_dao import CompanyProfileDao
from dao.postgresql.connect import connect
from dao.postgresql.stock_data_dao import Stockdatadao
import json

from service.yahooquery_service import get_company_profile_information, get_stock_data_by_yahoo_finance


def read_symbols_config():
    with open("./config/symbols.json", "r") as file:
        config = json.load(file)

    # Access the symbols from the config
    return config["company_symbols"], config["coin_symbols"]


if __name__ == "__main__":
    # connect postgres database
    postgresDb = connect()

    stock_data_dao = Stockdatadao(postgresDb)

    company_profile_dao = CompanyProfileDao(postgresDb)

    company_symbols, coin_symbols = read_symbols_config()

    # get company profile information

    for symbol in company_symbols:
        company_profile_model = company_profile_dao.select(symbol)

        if company_profile_model is None:
            company_profile_model = company_profile_dao.insert(get_company_profile_information(symbol))

        stock_data_list = get_stock_data_by_yahoo_finance(symbol, company_profile_model)

        for stock_data in stock_data_list:
            stock_data_dao.insert(stock_data)
        print("Inserted the stock data of symbol: " + symbol)

    postgresDb.close()
