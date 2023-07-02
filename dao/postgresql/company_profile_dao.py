import uuid

from model.company_profile import CompanyProfile


class CompanyProfileDao:

    def __init__(self, db):
        self.db = db

    def insert(self, model: CompanyProfile) -> CompanyProfile | None:
        cursor = self.db.cursor()
        try:
            sql = """INSERT INTO "Company_Profile" (id, symbol, address, city, state, zip, 
                                country, website, sector, industry) """ \
                  """VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (str(uuid.uuid4()), model.symbol, model.address, model.city, model.state, model.zip,
                   model.country, model.website, model.sector, model.industry)
            cursor.execute(sql, val)
            self.db.commit()
            print("Inserted company profile for symbol: " + model.symbol)
            return model
        except Exception as e:
            raise e
        finally:
            cursor.close()

    def select(self, symbol) -> None | CompanyProfile:
        cursor = self.db.cursor()
        try:
            sql = """SELECT address, city, state, symbol, 
                            zip, country, website, sector, industry, id 
                            FROM "Company_Profile" WHERE symbol = %s"""
            val = (symbol,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result is None:
                return None
            else:
                return CompanyProfile(address=result[0], city=result[1], state=result[2], symbol=result[3],
                                      zip=result[4], country=result[5], website=result[6], sector=result[7],
                                      industry=result[8], id=result[9])

        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()
