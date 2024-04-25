import requests
import json

def fetch_news(api_key):
    """
    Fetches news articles from the News API.
    """
    url = 'https://newsapi.org/v2/everything'
    parameters = {
        'q': 'Apple',  # or 'Apple' or any company
        'pageSize': 20,  # Number of articles to fetch
        'apiKey': api_key  # Your API key
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    # print(data) # Debug
    return data['articles']

def fetch_stock_data(api_key, symbol):
    """
    Fetches stock data from the Alpha Vantage API.
    """
    url = 'https://www.alphavantage.co/query'
    parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'apikey': api_key,
        'outputsize': 'compact'
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    # print(data) # Debug
    return data['Time Series (Daily)']