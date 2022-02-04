from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = '/Users/kinoko/Applications/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')

buy_item_timeout = time.time() + 5
after_5_minutes = time.time() + 10 * 5
name_list = []
price_list = []


items = driver.find_elements(By.CSS_SELECTOR, '#store b')

while True:
    cookie.click()
    if time.time() > buy_item_timeout:
        for item in items:
            try:
                item_name = item.text.split('-')[0].strip()
                name_list.append(item_name)
                item_price = item.text.split()[-1].replace(',', '').strip()
                price_list.append(item_price)

            except IndexError:
                pass

        reversed_item_name = list(reversed(name_list))
        reversed_item_price = list(reversed(price_list))

        for n in range(len(reversed_item_price)):
            money = driver.find_element(By.ID, 'money').text.replace(',', '').strip()
            if int(money) > int(reversed_item_price[n]):
                driver.find_element(By.ID, f'buy{reversed_item_name[n]}').click()
                break
        buy_item_timeout += 5

    if time.time() > after_5_minutes:
        score = driver.find_element(By.ID, 'cps')
        print(score.text)
        break
driver.quit()

test = 'cursor - 2,000'
price = int(test.split()[-1].replace(',','').strip())
print(type(price))
