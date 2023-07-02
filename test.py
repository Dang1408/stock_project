from yahooquery import Ticker
import json

from service.yahooquery_service import get_company_profile_information

# Read the config file
with open("./config/symbols.json", "r") as file:
    config = json.load(file)

# Access the symbols from the config
symbols = config["company_symbols"]

# Print the symbols
get_company_profile_information("VNINDEX")

