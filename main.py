import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameters = {
	"apiKey": "ab740822d6184234872d9add4b1b8a6e",
	"q": COMPANY_NAME
}
parameter = {
	"function": "TIME_SERIES_DAILY",
	"symbol": STOCK_NAME,
	"apikey": "NDTATOXM3PDGSF6D"
}

def get_news():
	responses = requests.get(NEWS_ENDPOINT, params = parameters)
	responses.raise_for_status()
	news = responses.json()["articles"][:3]
	return news

response = requests.get(STOCK_ENDPOINT, params = parameter)
response.raise_for_status()
get_news()
data = [value for (key, value) in response.json()["Time Series (Daily)"].items()]
if round((abs(float(data[1]["4. close"]) - float(data[0]["4. close"]))/float(data[0]["4. close"])) * 100, 4) > 5:
	NEWS = get_news()



#TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""