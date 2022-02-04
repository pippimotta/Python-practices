import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

LAT = 34.0702703
LON = 134.554843
API_KEY = '13f1ee0270162c49bc1398e3975ee70a'
ACCOUNT_ID = 'ACc79a007535e78fa3cfa8fcf32771d394'
TOKEN = '3dfe9c7f58405f56ef57617eeb63ba3c'
account_sid = ACCOUNT_ID
auth_token = TOKEN

parameter = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?', params=parameter)
response.raise_for_status()
data = response.json()
next_12_hour = data['hourly'][:12]
next_weather = [num['weather'][0]['id'] for num in next_12_hour]
if_rain = False
for condition in next_weather:
    if condition < 700:
        if_rain = True

if if_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)


    message = client.messages \
        .create(
        body="It's going to rain!Remember to bring your umbrella☔️muamua",
        from_='+18647079285',
        to='+817033181697'
    )

    print(message.status)


LAT_sh = 31.230391
LON_sh = 121.473701

API_KEY = '13f1ee0270162c49bc1398e3975ee70a'
ACCOUNT_ID = 'ACc79a007535e78fa3cfa8fcf32771d394'
TOKEN = '3dfe9c7f58405f56ef57617eeb63ba3c'
account_sid = ACCOUNT_ID
auth_token = TOKEN

parameter_sh = {
    'lat': LAT_sh,
    'lon': LON_sh,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}
response_sh = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?', params=parameter_sh)
response_sh.raise_for_status()
data_sh = response_sh.json()
next_12_hour_sh = data_sh['hourly'][:12]
next_weather_sh = [num['weather'][0]['id'] for num in next_12_hour_sh]
if_rain_sh = False
for condition in next_weather_sh:
    if condition < 700:
        if_rain_sh = True

if if_rain_sh:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)


    message = client.messages \
        .create(
        body="今天下雨☔，妈妈记得带伞！😘",
        from_='+18647079285',
        to='+8618221189370'
    )

    print(message.status)
