from datetime import datetime, timedelta
import requests
from data.env_vars import *
from data.debug_data import *
from twilio.rest import Client


def get_stock_value() -> dict:
    """ Gets the Stock value for the last days """
    if MODE == "DEBUG":
        return TSLA_STOCK_DATA

    url = ALPHAVANTAGE_API_URL
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": ALPHAVANTAGE_API_KEY
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def get_delta(data: dict) -> float:
    """ Check last 2 days of transactions and returns the delta in its close price """
    raw_data = data["Time Series (Daily)"]
    s_data = sorted(datetime.strptime(key, "%Y-%m-%d") for key in raw_data)
    stock_values = [float(raw_data[datetime.strftime(key, "%Y-%m-%d")]["4. close"]) for key in s_data[len(s_data)-2:]]
    return round((stock_values[1]/stock_values[0] - 1) * 100, 2)


def get_news() -> dict:
    """ Gets news for the stock company from the last day """
    if MODE == "DEBUG":
        return TSLA_NEWS_DATA

    url = NEWS_API_URL
    params = {
        "q": "Tesla",
        "from": datetime.strftime(datetime.now() - timedelta(days=1), "%Y-%m-%d"),
        "sortBy": "popularity",
        "pageSize": 5,
        "apiKey": NEWSAPI_API_KEY
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def get_latest_news(data) -> str:
    """ Formats the latest and most popular news as a string """
    top_3 = data["articles"][:3]
    formatted = [f"Headline: {news["title"]}\nBrief: {news["description"]}\n" for news in top_3]
    text = ""
    for item in formatted:
        text += item
    return text


def send_whatsapp(content: str):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        to=TWILIO_TO_NUMBER,
        body=content
    )
    print(message.status)


stock_info = get_stock_value()
delta = get_delta(stock_info)
if abs(delta) >= 0.1:
    direction = "🔺" if delta > 0 else "🔻"
    alert = f"{STOCK}: {direction} {delta}% ({stock_info["Meta Data"]["3. Last Refreshed"]})\n"

    new_info = get_news()
    alert += get_latest_news(new_info)
    send_whatsapp(alert)
    print(alert)
