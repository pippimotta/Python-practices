from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/kinoko/Applications/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('https://www.python.org/')
dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')#多個class name中間用空格區分 注意辨認 找最特殊的一個
events = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')
dates = [date.text for date in dates]
events =[event.text for event in events][1:]
final_dic ={}
for n in range(len(dates)):
    final_dic[n] = {
        'time': dates[n],
        'event': events[n]
    }
print(final_dic)
driver.quit()

