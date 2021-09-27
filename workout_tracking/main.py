import requests
from datetime import datetime, timedelta
import string
import os


APP_ID = os.environ['app_id']
API_KEY = os.environ['api_key']

exercise_endpoint = os.environ.get(EXERCISE_ENDPOINT)

gender = 'male'
weight = '90'
height = '180'
age = 31
query = 'I did 30 pushups and 20 biceps. Additionally, I ran 34 km.'

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_body = {
    'query': query,
    'gender': gender,
    'weight_kg': weight,
    'height_cm': height,
    'age': age
}

response = requests.post(url=exercise_endpoint, json=exercise_body, headers=exercise_headers)
print(response.text)
response_json = response.json()

sheety_endpoint = os.environ.get(SHEETY_ENDPOINT)
date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%H:%M:%S')

for exercise in response_json['exercises']:
    exercise_name = exercise['user_input']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    workout_json = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise_name.title(),
            'duration': duration,
            'calories': calories
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=workout_json)
    print(sheety_response.text)
