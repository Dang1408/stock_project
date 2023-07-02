class CompanyProfile:
    def __init__(self, city, address, state, website, industry, symbol, country, sector, zip, id=None):
        self.city = city
        self.address = address
        self.state = state
        self.website = website
        self.industry = industry
        self.symbol = symbol
        self.country = country
        self.sector = sector
        self.zip = zip
        self.id = id

    def __str__(self) -> str:
        return f"CompanyProfile(city={self.city}, address={self.address}, state={self.state}, website={self.website}, " \
               f"industry={self.industry}, symbol={self.symbol}, country={self.country}, sector={self.sector})"


