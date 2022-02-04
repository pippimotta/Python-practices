import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os
MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

EXPECT_PRICE = 6000
URL = 'https://www.amazon.co.jp/TTWO-%E6%8A%98%E3%82%8A%E3%81%9F%E3%81%9F%E3%81%BF%E3%83%87%E3%82%B9%E3%82%AF-%E5%B9%8580%C3%97%E5%A5%A5%E8%A1%8C46%C3%97%E9%AB%98%E3%81%9571cm-%E5%82%B7%E3%83%BB%E6%B1%9A%E3%82%8C%E3%83%BB%E6%B0%B4%E5%88%86%E3%83%BB%E7%86%B1%E3%81%AB%E5%BC%B7%E3%81%84-%E3%82%A2%E3%82%A6%E3%83%88%E3%83%89%E3%82%A2%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB/dp/B09F62665Y/ref=sr_1_12?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E6%9C%BA&qid=1635087144&sr=8-12'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
ACCEPTED_LANGUAGE = 'ja-JP,en;q=0.5'
headers ={
    'user-agent': USER_AGENT,
    'accept-language': ACCEPTED_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
price_str = soup.find(name='span', class_='a-offscreen').getText()
price_int = int(price_str.strip('￥').replace(',', ''))
good_title = soup.find(name='span', id='productTitle').getText().strip('')
print(good_title)
if price_int < EXPECT_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='mushroomzly@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n Your dream desk is now at {price_int}\n{URL}!"
        )

