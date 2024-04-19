import requests
import datetime
import os
APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]
# "f727094e0e2f8b5c1895ba12a447afc9"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = os.environ["ENV_SHEETY_API"]
TOKEN = os.environ["ENV_AUTHORIZATION"]
exercise_text = input("Tell me which exercises you are doing ")
GENDER = "Male"
WEIGHT_KG = 60
HEIGHT_CM = 176.59
AGE = 19
header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}


parameters    = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(endpoint, json=parameters, headers=header)
result = response.json()
print(result)
workout = result['exercises']
calories = workout[0]['nf_calories']
duration = workout[0]['duration_min']
exercise = workout[0]['name'].title()
raw_date = datetime.datetime.now()
date = raw_date.strftime("%d/%m/%Y")
time = raw_date.strftime("%X")
shetty_params = {
    "workout": {
        'date': date,
        'time': time,
        'exercise': exercise,
        'duration': duration,
        'calories': calories
    }
}
username = "Olakunle"
password = "alex123@#$"
headers = {
    "Authorization": TOKEN
}
shetty_post = "https://api.sheety.co/924e1ccde52593b39b4290e14ce64aff/myWorkouts/workouts"
post_response = requests.post(url=shetty_post, json=shetty_params, headers=headers)
print(post_response.json())
