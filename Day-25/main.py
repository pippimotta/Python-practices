# with open('weather_data.csv') as f:
#     data= f.readlines()
#     print(data)
#
# import csv
# with open('weather_data.csv') as f:
#     data = csv.reader(f) #創建一個csv object可以拿來用
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))

import pandas
data = pandas.read_csv('weather_data.csv')
# get data from row
# print(data[data.temp == 14])
print(data[data.day == 'Monday']) #get the column you want to search through --check for the role is Monday
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp* 9/5 + 32
# print(monday_temp_F )

# create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# new_data = data.to_csv('new_data.csv')
