from flight_data import FlightData


flight_data = FlightData()
departure_date = input("What's your departure date to fly? (format: YYYY-MM-DD) ")
flight_data.scan_deals(departure_date)