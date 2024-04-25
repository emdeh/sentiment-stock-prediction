import os
from fetch_data import fetch_news, fetch_stock_data
from mongo_utils import save_news_data_to_db, save_stock_data_to_db, clear_collection
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Initialise environment variables
mongo_uri = os.getenv('MONGO_URI')
db_name = os.getenv('DB_NAME')
news_collection = os.getenv('NEWS_COLLECTION_NAME')
stock_collection = os.getenv('STOCK_COLLECTION_NAME')
news_api_key = os.environ.get('NEWS_API_KEY')
stocks_api_key = os.environ.get('STOCKS_API_KEY')

# Uncomment to clear a collection for debugging purposes
#clear_collection(mongo_uri, db_name, news_collection)
#clear_collection(mongo_uri, db_name, stock_collection)

# Fetch the news data
news_data = fetch_news(news_api_key)

# Store news data in MongoDB and perform sentiment analysis
save_news_data_to_db(news_data, mongo_uri, db_name, news_collection, perform_sentiment_analysis=True)

# Fetch stock data
stock_data = fetch_stock_data(stocks_api_key, 'AAPL')

# Store stock data in MongoDB
save_stock_data_to_db(stock_data, mongo_uri, db_name, stock_collection)