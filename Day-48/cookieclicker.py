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
five_min = time.time() + 60 * 5
while True:
    cookie.click()

    if time.time() > buy_item_timeout:
        items = driver.find_elements(By.CSS_SELECTOR, '#store div')
        for item in items[::-1]:
            if item.get_attribute("class") != "grayed":
                item.click()
                break

        buy_item_timeout += 5

    if time.time() > five_min:
        score = driver.find_element(By.ID, 'cps')
        print(score.text)
        break

driver.quit()