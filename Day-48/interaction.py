from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/kinoko/Applications/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# article_number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_number.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# # all_portals.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)
# # go = driver.find_element(By.NAME, 'go')
# # go.click()
#
# # driver.quit()
driver.get('http://secure-retreat-92358.herokuapp.com/')
f_name = driver.find_element(By.NAME, 'fName')
l_name = driver.find_element(By.NAME,'lName')
e_mail = driver.find_element(By.NAME,'email')

f_name.send_keys('Leni')
l_name.send_keys('Chang')
e_mail.send_keys('adeleid6@yahoo.com')
e_mail.send_keys(Keys.ENTER)