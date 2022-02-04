#抓取火車站代碼 - 原始代碼，站名由標籤button包起來
#將車站代碼和車站名稱放在dict形態的變量中；通過站名直接取得車站代碼
#如何輸入表單&傳送表單：輸入框被form的標籤包圍，標籤中有屬性method= post 向主機傳送request
#form標籤裡的input標籤內容即為要傳送給主機的資料
#屬性action中的<form id="queryForm" action="/tra-tip-web/tip/tip001/tip112/querybytime" method="post">
#action中的網址為回傳表單資訊的網址（相對），要加入台鐵網址的domain
#input csrf防詐欺 需要把<input type="hidden" name="_csrf" value="7cfae347-afb6-43e3-a095-57aef85aa73c">後的value一起發送
#進行表單選擇操作 -開發人員工具- network -querybytime - headers-將表單傳送主機的網址連結
#下方formdata為準備回傳的參數資料：key-value

# 帳號密碼
#get 取得網頁- 準備回傳表單及回傳網址 -分析回傳結果的網頁內容
import requests
from bs4 import BeautifulSoup
import time
url = 'https://tip.railway.gov.tw/tra-tip-web/tip'
staDic = {} #聲明字典變量 存儲火車站及車站代碼
today = time.strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '12:00'

def getTrip():
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url錯誤' + url)
        return
    soup = BeautifulSoup(resp.text, 'html5lib')#取得soup物件

    #取得車站名稱及車站代碼放入字典中
    stations = soup.find(id='cityHot').ul.find_all('li') #ul為子標籤

    for station in stations:
        stationName = station.button.text #車站名字被button標籤包圍，用text取字串
        stationId = station.button['title'] #用中括弧取得屬性的值
        staDic[stationName] = stationId #建立車站名稱對應車站代碼的字典

    csrf = soup.find(id='queryForm').find('input', {'name': '_csrf'})['value'] #取得csrf代碼


    #準備回傳表單（字典型態）開發人員工具- network -querybytime - headers-將表單傳送主機的網址連結
    formData = {
        'trainTypeList': 'ALL',
        'transfer': 'ONE',
        'startOrEndTime': 'true',
        'startStation': staDic['臺北'],
        'endStation': staDic['新竹'],
        'rideDate': today,
        'startTime': sTime,
        'endTime': eTime,
        '_csrf': csrf
    }

    #取得回傳網址，將以上表單回傳
    queryUrl = soup.find(id ='queryForm')['action']
    #使用post函式回傳
    qresp = requests.post('https://tip.railway.gov.tw' + queryUrl, data=formData ) #post函式中第一個參數為domain+回傳表單網址
    qSoup = BeautifulSoup(qresp.text, 'html5lib')
    #回傳清單放在標籤tr屬性trip-column中
    trs = qSoup.find_all('tr', 'trip-column')
    for tr in trs:
        td = tr.find_all('td')
        print('%s: %s, %s' % (td[0].ul.li.a.text, td[1].text, td[2].text))
getTrip()






