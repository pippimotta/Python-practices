# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# chrome_driver_path = '/Users/kinoko/Applications/chromedriver'
# s = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=s)
# driver.minimize_window()
# driver.get('https://www.amazon.co.jp/TTWO-%E6%8A%98%E3%82%8A%E3%81%9F%E3%81%9F%E3%81%BF%E3%83%87%E3%82%B9%E3%82%AF-%E5%B9%8580%C3%97%E5%A5%A5%E8%A1%8C46%C3%97%E9%AB%98%E3%81%9571cm-%E5%82%B7%E3%83%BB%E6%B1%9A%E3%82%8C%E3%83%BB%E6%B0%B4%E5%88%86%E3%83%BB%E7%86%B1%E3%81%AB%E5%BC%B7%E3%81%84-%E3%82%A2%E3%82%A6%E3%83%88%E3%83%89%E3%82%A2%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB/dp/B09F62665Y/ref=sr_1_12?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E6%9C%BA&qid=1635087144&sr=8-12')
# # price = driver.find_element(By.ID, 'price_inside_buybox')
# price = driver.find_element(By.XPATH,'//*[@id="price_inside_buybox"]')
# print(price.text)
#
# driver.quit()
list= [1,2,3,4,5,6]
list2 = ['1','2','3','4','5','6']
dict = dict(zip(list, list2))
print(dict)