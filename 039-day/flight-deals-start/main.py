#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    codes = flight_search.get_destination_codes(city_names)
    print(codes)
    print('---------------------------')
    # data_manager.update_destination_codes(codes)
    # sheet_data = data_manager.get_destination_data()

# today = datetime.now() + timedelta(1)
# six_month_from_today = datetime.now() + timedelta(6 * 30)

# for destination in sheet_data:
#     flight = flight_search.check_flights(
#         ORIGIN_CITY_IATA,
#         destination["iataCode"],
#         from_time=today,
#         to_time=six_month_from_today
#     )

#     if flight.price < destination["lowestPrice"]:
#         notification_manager.send_sms(
#             message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
#         )