import requests
from bs4 import BeautifulSoup

resp = requests.get('https://code-gym.github.io/spider_demo/')# 取得網頁資料
soup = BeautifulSoup(resp.text, "html5lib")#response交給Bea解析，後者為分析器名稱
#print(soup.find('h1'))
#print(soup.find('h1').text) #.text為單獨取出文字
print(soup.h1.text)

#find_all，找到所有h3標籤並且回傳list
for h3 in soup.find_all('h3'):
    print(h3.a)#用標籤a選出包含超鏈接的結果

#class屬性

for title in soup.find_all('h3', 'post-title'):
    print(title.a)

#用key-value尋找更多屬性
for cat in soup.find_all('a', {'class': 'post-category', 'class': 'cat-1'}):
    print(cat)

#抓取部落格文章標題和資訊 移除空白與跳行符號&取得文本內容用stripped_strings,生成的是generator物件，需要用for一個一個取出
for posts in soup.find_all('div', 'post-body'):
    for post in posts.stripped_strings:
        print(post)

#抓取父節點parent
nav = soup.find(id = 'nav') #取得id名為nav的元素
header = nav.parent
print(header) #標籤id為nav的元素

#抓取兄弟節點sibling
jav = soup.find('li', 'cat-2')
print(jav)
print(jav.previous_sibling)
print(jav.next_sibling)

#抓取子節點children
ul = soup.find('ul')
for li in ul.children: #用屬性children取得所有標籤名為li的元素
    print(li.find('a')) #列印超鏈接標籤