import requests
from bs4 import BeautifulSoup

def Travelcloud(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser') #獲取html內容
    if resp.status_code != 200:
        print("url錯誤")
        return
    #1 result = soup.find_all('h3', limit=4) #limit控制爬下來的數量
    # print(result)

    #2 尋找多個標籤時用list['h3','p']
    #result = soup.find_all(['h3', 'p'] , limit = 4)
    #print(result)

    #3 尋找子節點
    #result = soup.find('h3', itemprop = 'headline')
    #print(result.select('a'))

    #4 搜尋網頁中符合指定的HTML標籤及css屬性值的所有節點
    #description = soup.find_all('p', class_= 'summary')
    #print(description)

    #5 向上搜尋标签为h3的父節點
    #result = soup.find('a', itemprop = 'url')
    #parents = result.find_parents('h3')
    #print(parents)

    #6 搜寻兄弟节点
    #result = soup.find('h3', itemprop='headline')
    #siblings = result.find_next_siblings('p')
    #print(siblings)

    #取得属性值 超链接
    #titles = soup.find_all('h3', itemprop='headline')
    #for title in titles:
    #print(title.select_one('a').get('href'))

    #取得文字
    titles = soup.find_all("h3", itemprop="headline")
    for title in titles:
        print(title.select_one("a").getText())

Travelcloud('https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/?&page=1')

#soup作為一個已經包含整個網頁html碼的物件， 用find()等方法進行節點的搜尋


