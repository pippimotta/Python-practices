import pandas
gray = 0
red = 0
black = 0
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# primary_fur_color = data['Primary Fur Color'].tolist()
# for color in primary_fur_color:
#     if color == 'Gray':
#         gray += 1
#     if color == 'Cinnamon':
#         red += 1
#     if color == 'Black':
#         black += 1
# color_dic = {'Fur Color': ['grey', 'red', 'black'], 'Count': [gray, red, black]}

grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_count = len(data[data['Primary Fur Color'] == 'Black'])
color_dic = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey_count, red_count, black_count]
}

df = pandas.DataFrame(color_dic)
df.to_csv('squirrel_count.csv')
