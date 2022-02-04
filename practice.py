#使用Selenium抓取主機回傳後的html，交給beautifulsoup解析
#使用selenium抓取回傳後的html，由selenium取得html元素值
#Xpath

#加入參數headless使瀏覽器在後台作業， 不彈出視窗
from bs4 import BeautifulSoup
from selenium import webdriver
try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options, executable_path= '/Users/pilzz/Desktop/pyyyy/chromedriver/chromedriver')
    chrome.set_page_load_timeout(10) #等待10s使網頁正常載入
    chrome.get('https://code-gym.github.io/spider_demo/')
    soup = BeautifulSoup(chrome.page_source, 'html5lib')
    print(soup.find('h1').text)

#讓程式自動點擊文章標題連結，之後抓取英文標題文字，使用xpath方法：結構樹中特定節點位置：開發人員工具-copy XPath
#點擊文章標題進入文章頁面 - 找到文章標題連結的元素位置
    chrome.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/div/h3').click()
    print(chrome.find_element_by_xpath('//*[@id="post-header"]/div[2]/div/div/h1').text)
finally:#關閉瀏覽器
    chrome.quit()




