import requests

serach_api = "*"
API_KEY = "*"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.search_api = serach_api
        self.headers = {
            'accept': 'application/json',
            'apikey': API_KEY
            }
    
    def get_destination_codes(self, iata_code):
        params = {
            'term':iata_code,
            'locale':'en-US',
            'location_types':'airport',
            'limit':10,
            'active_only':True
        }
        
        response = requests.get(self.search_api, params=params, headers=self.headers)
        if(response.status_code == 200):
            return response.json()['locations']