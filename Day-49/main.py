from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

FB_MAIL = 'mushroomzly@gmail.com'
FB_PASSWORD = 'muszha__615'

chrome_driver_path = '/Users/kinoko/Applications/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://tinder.com/')
driver.set_window_size(720,720)
driver.implicitly_wait(2)
log_in = driver.find_element(By.XPATH, '//*[@id="q-274726726"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
log_in.click()
time.sleep(2)
fb_log_in = driver.find_element(By.XPATH, '//*[@id="q-53386290"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_log_in.click()


base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)
mail = driver.find_element(By.XPATH, '//*[@id="email"]')
mail.send_keys(FB_MAIL)
password = driver.find_element(By.XPATH,'//*[@id="pass"]')
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
