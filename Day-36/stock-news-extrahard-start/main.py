import requests
import html
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = 'TDF3SASTVRIDJE8Q'
parameters_stock = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'TSLA',
    'apikey': stock_api_key
}
stock_response = requests.get(url='https://www.alphavantage.co/query?', params=parameters_stock)
stock_response.raise_for_status()
data_stock = stock_response.json()
stock_price_dict = data_stock['Time Series (Daily)']
stock_price_date = list(stock_price_dict.keys())[:2]
stock_price_daily_close = [float(stock_price_dict[date]["5. adjusted close"]) for date in stock_price_date]

if_fluctuated = False
fluctuation = abs((stock_price_daily_close[0] - stock_price_daily_close[1]) / stock_price_daily_close[0])
if stock_price_daily_close[0] > stock_price_daily_close[1]:
    pattern = '🔺'
else:
    pattern = '🔻'
fluc_per = round(fluctuation * 100, 2)
news_api_key = 'a6f0b4a9603f4f058cfde6d2d2dc530e'
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if fluctuation > 0.01:
    parameters_news = {
        'q': 'TESLA',
        'Date published': stock_price_date[0],
        # 'sources': 'https://www.tradingview.com/symbols/NASDAQ-TSLA/',
        'apiKey': news_api_key,
        'sortBy': 'popularity'
    }

    news_response = requests.get(url='https://newsapi.org/v2/everything?', params=parameters_news)
    news_response.raise_for_status()
    data_news = news_response.json()['articles']
    news_3 = data_news[0:3]

    news_title = [news['title'] for news in news_3]
    news_description = [html.unescape(news['description']).rstrip("\\") for news in news_3]

    account_sid = 'ACc79a007535e78fa3cfa8fcf32771d394'
    auth_token = '3dfe9c7f58405f56ef57617eeb63ba3c'
    client = Client(account_sid, auth_token)
    for i in range(3):
        message = client.messages \
            .create(
            body=f"TSLA: {pattern}{fluc_per}%\nHeadline:{news_title[i]}\nBrief:{news_description[i]}",
            from_='+18647079285',
            to='+817018127929'
        )

    print(message.status)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """
