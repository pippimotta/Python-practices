import requests
from pprint import pprint

SHEETY_ENDPOINT = 'https://api.sheety.co/61e68f1640a4bb6bb366c61e70d9963b/flightDeal/工作表1'
SHEETY_APIKEY = 'Basic TXVzaHJvb21aOnBvcDYxNQ=='
headers_sheet = {'Authorization': SHEETY_APIKEY}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers_sheet)
        self.destination_data = response.json()
        return self.destination_data

    def upgrade_destination_code(self):
        for city in self.destination_data:
            new_data = {
                '工作表1': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(url=f'{SHEETY_ENDPOINT}/{city["id"]}', json=new_data, headers=headers_sheet)