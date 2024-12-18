import requests
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "JBLFEPYMP8ICDA0I"
NEWS_API_KEY = "9dcdd874eada495899d6592baf6f631c"
STOCK_PARAMS = {"function": "TIME_SERIES_DAILY", "symbol": STOCK, "outputsize": "full", "apikey": STOCK_API_KEY}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_API_ENDPOINT, params=STOCK_PARAMS)

stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

diff_percentage = (difference / float(yesterday_closing_price)) * 100
print(diff_percentage)

if diff_percentage >= 3:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_API_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[0:3]
    print(three_articles)
    formatted_article = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in three_articles]
    print(formatted_article)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
