import requests
from datetime import datetime

day = datetime(year=2021, month=9, day=28)
print(day.strftime("%Y%m%d"))

USER_NAME = 'mushroomzombie'
TOKEN = '%8Wj1c#P(+5zPeCO'
GRAPH_ID = 'mushroomsjourney'
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs'
#
graph_configuration = {
    'id': 'mushroomsjourney',
    'name': 'coding_graph',
    'unit': 'hour',
    'type': 'float',
    'color': 'ajisai'
}
#
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)


pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

pixel_data = {
    'date': day.strftime("%Y%m%d"),
    'quantity': '8'

}

pixel_update_data = {
    'date': day.strftime("%Y%m%d"),
    'quantity': '8'

}

pixel_update_endpoint = f'{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{day.strftime("%Y%m%d")}'
response = requests.delete(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
print(response.text)
