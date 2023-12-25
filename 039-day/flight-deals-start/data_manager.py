import requests
sheet_end_point = "*"
BEARER_TOKEN = "Bearer ***"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.api_end_point = sheet_end_point
        self.headers = {
            "Authorization": BEARER_TOKEN
        }
    
    def get_sheet_data(self):
        response = requests.get(self.api_end_point, headers=self.headers)
        if(response.status_code == 200):
            return response.json()["prices"]