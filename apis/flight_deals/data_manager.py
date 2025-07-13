import requests
from flight_search import FlightSearch
from data.env_vars import SHEETY_URL, SHEETY_TOKEN


class DataManager:
    """ This class is responsible for talking to the Google Sheet. """

    def __init__(self):
        self.url = SHEETY_URL
        self.header = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
        self.search = FlightSearch()

    def get_prices(self) -> list:
        """ Returns the spreadsheet data as a list of dicts"""
        response = requests.get(url=self.url, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]

    def update_iata_code(self, city_id: str, iata_code: str):
        """Updates the IATA code for a given city"""
        url = self.url + f"/{city_id}"
        data = {
            "price": {"iataCode": iata_code}
        }
        response = requests.put(url=url, json=data, headers=self.header)
        response.raise_for_status()
        print(response.json())

    def update_prices(self, city_id: str, new_price: float):
        """Updates the lowestPrice for a given city (if it's a bargain)"""
        url = self.url + f"/{city_id}"
        data = {
            "price": {"lowestPrice": new_price}
        }
        response = requests.put(url=url, json=data, headers=self.header)
        response.raise_for_status()
        print(response.json())


