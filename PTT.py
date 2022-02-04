# 取得今天所有發文（推文數>10)的標題
# 取得推文數，文章標題與日期-html/以及上一頁的超連結
# 每個文章由標籤div和class名稱r-rent包起來；可以通過div與title取得標題文字
# 推文數由class名稱為nrec包起來
# 日期：class為date；外包class為meta
# 「上一頁」標籤排序為第2；list索引值為1

import requests
from bs4 import BeautifulSoup
import time

today = time.strftime('%m/%d').lstrip('0')  # 取得今日時間字串；移除%m最左端的0


def pttNBA(url):
    resp = requests.get(url) #用函式requests.get()連到PTT版
    if resp.status_code != 200: #判斷是否連接正確
        print('URL發生錯誤：' + url)
        return

    soup = BeautifulSoup(resp.text, 'html5lib')
    paging = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]['href']

    articles = []
    rents = soup.find_all('div', 'r-ent')
    for rent in rents:
        title = rent.find('div', 'title').text.strip()  # 取得文章標籤並用strip()去掉空白字元
        count = rent.find('div', 'nrec').text.strip()
        date = rent.find('div', 'meta').find('div', 'date').text.strip()
        article = '%s %s:%s' % (date, count, title)

        try:
            if today == date and int(count) > 10:
                articles.append(article)

        except:
            if today == date and count == '爆':
                articles.append(article)

    if len(articles) != 0:
        for article in articles:
            print(article)
        pttNBA('https://www.ptt.cc' + paging)

    else:
        return


pttNBA('https://www.ptt.cc/bbs/NBA/index.html')

