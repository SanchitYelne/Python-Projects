import requests
from datetime import datetime

APP_ID = "b6aa3250"
API_KEY = "0f2bf2263437c6295675385cdf365fa1"

GENDER = "male"
WEIGHT_KG = "71"
HEIGHT_CM = "181"
AGE = "20"

USER_NAME = "sanchit_yelne"
PASSWORD = "@sanchit13"

TOKEN = "c2FuY2hpdF95ZWxuZTpAc2FuY2hpdDEz"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did : ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    # "weight": WEIGHT_KG,
    # "height": HEIGHT_CM,
    "age": AGE
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=headers)
result = nutritionix_response.json()
print(result)

today = datetime.now()
formatted_date = today.strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": formatted_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_endpoint = "https://api.sheety.co/813f619b2517dfb892f792f26a148d36/myWorkouts/workouts"

# sheet_responses = requests.post(url=sheet_endpoint, json=sheet_inputs)
# print(sheet_responses.text)

sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      USER_NAME,
      PASSWORD
  )
)

bearer_headers = {
"Authorization": f"Bearer {TOKEN}"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

