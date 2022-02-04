import requests
from datetime import datetime
MY_LAT = 34.070271
MY_LNG = 134.554840
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
# data = response.json()
# print()
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position = (latitude,longitude)
# print(iss_position)
# if response.status_code == 404:
#     raise Exception('That resource does not exist')
# elif response.status_code == 401:
#     raise Exception('You are not authorised to access this data')
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
      'formatted': 0

}
response = requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sun_rise = data['results']['sunrise'].split('T')[1].split(':')[0]
sun_set = data['results']['sunset'].split('T')[1].split(':')[0]
print(sun_rise)
print(sun_set)
time_now = datetime.now()
print(time_now.hour)
