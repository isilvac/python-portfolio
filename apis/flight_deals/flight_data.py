from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


class FlightData:
    """ This class is responsible for structuring the flight data. """

    def __init__(self):
        self.dm = DataManager()
        self.fs = FlightSearch()
        self.notifier = NotificationManager()

        # Reads the file and updates any missing code
        locations = self.dm.get_prices()
        self.fill_city_code(locations)

    def fill_city_code(self, city_list: list):
        """Checks missing IATA codes and updates them"""
        for city in city_list:
            if city["iataCode"] == "":
                code = self.fs.get_city_code(city["city"])
                self.dm.update_iata_code(city["id"], code)

    def scan_deals(self, departure: str):
        """Takes the spreadsheet and checks prices per destination looking for a good offer (lower price)
            If it finds something lower, sends an SMS and updates the price in the spreadsheet"""
        destinations = self.dm.get_prices()
        offers = []

        for dest in destinations:
            city_id = dest["id"]
            city = dest["city"]
            city_code = dest["iataCode"]
            current_price = float(dest["lowestPrice"])

            print(f"Looking deals for {city_code} below ${current_price}")
            deals = self.fs.get_flight_prices(destination=city_code, departure=departure)
            print(deals)
            ticketed_departure = deals[0]["itineraries"][0]["segments"][0]["departure"]["at"]
            deal_price = float(deals[0]["price"]["grandTotal"]) or dest["lowestPrice"]

            if deal_price < current_price:
                print(f"New lowest price: ${deal_price} with departure in {departure}")
                offers.append({"city": city, "price": deal_price, "departure": ticketed_departure})
                self.dm.update_prices(city_id=city_id, new_price=deal_price)
        if len(offers) > 0:
            self.send_notifications(offers)

    def send_notifications(self, offers: list):
        """For a list of offers, it sends an SMS per destination"""
        for notif in offers:
            message = f"There's a new lower price to {notif['city']} for {notif['price']} USD with departure on {notif['departure']}"
            self.notifier.send_sms(message)
