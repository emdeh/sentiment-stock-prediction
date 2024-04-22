import requests
import json

def fetch_news(api_key):
    """
    Fetches news articles from the News API.
    """
    url = 'https://newsapi.org/v2/everything'
    parameters = {
        'q': 'stock market',  # or 'Apple' or any company
        'pageSize': 20,  # Number of articles to fetch
        'apiKey': api_key  # Your API key
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    # print(data) # Debug
    return data['articles']
