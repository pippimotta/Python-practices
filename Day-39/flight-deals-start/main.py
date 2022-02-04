from datetime import datetime, timedelta

from flight_search import FlightSearch
from data_manager import DataManager

flight_research = FlightSearch()
data_manager = DataManager()
city_data = data_manager.get_destination_data()
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=6 * 30)
print(city_data)
for city_info in city_data:
    city_info['iataCode'] = flight_research.get_destination_code(city_info['city'])
    data_manager.upgrade_destination_code()
    flight_data = flight_research.check_flights('LON', city_info['iataCode'], tomorrow, six_months_from_today)
    print(flight_data)





