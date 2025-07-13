import requests
from data.env_vars import AMADEUS_API_KEY, AMADEUS_API_SECRET, AMADEUS_DOMAIN
from datetime import datetime


class FlightSearch:
    """ This class is responsible for talking to the Flight Search API. """
    def __init__(self):
        self.api_key = AMADEUS_API_KEY
        self.api_secret = AMADEUS_API_SECRET
        self.domain = AMADEUS_DOMAIN

        # set them as null until we require them
        self.token = None
        self.token_expiration = None

    def get_token(self) -> str:
        """Returns the existent token or get it from the service (if outdated)"""
        if self.token_expiration and (int(self.token_expiration) > int(datetime.now().timestamp()) + 10):
            return self.token

        url = self.domain + "/v1/security/oauth2/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        params = f"grant_type=client_credentials&client_id={AMADEUS_API_KEY}&client_secret={AMADEUS_API_SECRET}"

        response = requests.post(url=url, data=params, headers=header, verify=False)
        response.raise_for_status()
        self.token = response.json()["access_token"]
        self.token_expiration = int(datetime.now().timestamp()) + int(response.json()["expires_in"])

        return response.json()["access_token"]

    def get_city_code(self, query: str) -> str:
        """Returns the IATA Code for a given city"""
        url = self.domain + "/v1/reference-data/locations/cities"
        params = {"keyword": query}
        header = {"Authorization": f"Bearer {self.get_token()}"}

        response = requests.get(url=url, params=params, headers=header)
        response.raise_for_status()
        for city in response.json()["data"]:
            if city["name"].lower() == query.lower():
                return city["iataCode"]
        return ""

    def get_flight_prices(self, destination: str, departure: str) -> dict:
        """Returns the data with the flight offers to the given destination and a given departure date"""
        url = self.domain + "/v2/shopping/flight-offers"
        header = {"Authorization": f"Bearer {self.get_token()}"}
        params = {
            "originLocationCode": "SCL",
            "destinationLocationCode": destination,
            "departureDate": departure,
            "currencyCode": "USD",
            "adults": 1,
            "max": 1
        }
        response = requests.get(url=url, headers=header, params=params)
        response.raise_for_status()
        return response.json().get("data", {})
