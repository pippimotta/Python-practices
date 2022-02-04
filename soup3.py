#翻页
#爬内容

import requests
from bs4 import BeautifulSoup
for i in range(1, 15):
    resp = requests.get('https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/?&page=' + str(i))
    soup = BeautifulSoup(resp.text, 'html5lib')
    if resp.status_code != 200:
        print('url出错')

    for info in soup.find_all('p', {'itemprop': 'description', 'class': 'summary'}):
        for des in info.stripped_strings:
            print(des)


