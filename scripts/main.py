import os
from fetch_news import fetch_news
from mongo_utils import get_news_from_db, save_data_to_db
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Initialise environment variables
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
API_KEY = os.environ.get('NEWS_API_KEY')

# Fetch the news data
news_data = fetch_news(API_KEY)

# Store news data in MongoDB
save_data_to_db(news_data, MONGO_URI, DB_NAME, COLLECTION_NAME, perform_sentiment_analysis=True)

# Fetch news data from MongoDB
get_news_from_db(DB_NAME, COLLECTION_NAME, MONGO_URI)