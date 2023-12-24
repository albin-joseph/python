import requests
from datetime import datetime

APP_ID = "***"
API_KEY = "***	"

base_url = "https://trackapi.nutritionix.com/"

exercise_endpoint = "v2/natural/exercise"

natural_language_endpoint = "v2/natural/nutrients"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": "Female",
    "weight_kg": "76",
    "height_cm": "175",
    "age": "29"
}

exercise_api = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(exercise_api, json=parameters, headers=headers)
result = response.json()
print(result)

################### Start of Step 4 Solution ######################
sheet_endpoint = "https://api.sheety.co/dfc12b16014e0535ccc53faaf6530e37/myWorkoutsAlbin/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
"Authorization": "Bearer *****"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)