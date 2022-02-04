import requests
from datetime import datetime
import os

GENDER = 'female'
WEIGHT_KG = 47
HEIGHT_CM = 162
AGE = 24
#
os.environ['APP_ID'] = 'd7727315'
os.environ['APP_KEY'] = 'd2a5fd48300fcc4c800c61e961ff7150'
os.environ['AUTHOR'] = 'Basic TXVzaHJvb206bWFpemg='

application_id = os.environ.get('APP_ID')
application_key = os.environ.get("APP_KEY")
auth = os.environ.get('AUTHOR')

query = input('Tell me which exercises you did?\n')
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
ex_parameters = {
    'query': query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers_app = {
    'x-app-id': application_id,
    'x-app-key': application_key,
}
response_ex = requests.post(url=exercise_endpoint, json=ex_parameters, headers=headers_app)
response_ex.raise_for_status()

ex_data = response_ex.json()['exercises']
ex_type = [ob['name'].title() for ob in ex_data]
ex_duration = [ob['duration_min'] for ob in ex_data]
ex_calories = [ob['nf_calories'] for ob in ex_data]

sheety_endpoint = 'https://api.sheety.co/84afdefeb24074a66c77e7eff398a0df/myWorkouts/workouts'

current_date = datetime.today().strftime('%x')
current_time = datetime.today().strftime('%X')

for i in range(len(ex_type)):
    add_parameters = {
        'workout': {
            'date': current_date,
            'time': current_time,
            'exercise': ex_type[i],
            'duration': ex_duration[i],
            'calories': ex_calories[i]
        }
    }

    headers_sheet = {
        "Authorization": auth
    }
    response_sheet = requests.post(url=sheety_endpoint, json=add_parameters, headers=headers_sheet)

    print(response_sheet.text)
