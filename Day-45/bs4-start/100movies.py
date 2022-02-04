from bs4 import BeautifulSoup

with open('website.html',encoding='utf-8') as mp:
    mt = mp.read()
    soup = BeautifulSoup(mt, 'html.parser')
movies = soup.find_all(name='h3', class_='jsx-4245974604')

movie_list = [movie.getText() for movie in movies]
movie_list.reverse()

with open('Best movies list', 'w') as bl:
    for item in movie_list:
        bl.write(f'{item} \n')


