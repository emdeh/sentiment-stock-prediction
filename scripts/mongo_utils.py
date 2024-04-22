import os
from pymongo import MongoClient
from contextlib import contextmanager
from analyse_sentiment import analyse_sentiment

@contextmanager
def get_mongo_client(mongo_uri):
    """
    Context manager to handle MongoDB client connection.
    Used in the other functions to handle the client connection.
    Ensures that the client connection is properly closed after use.
    """
    client = MongoClient(mongo_uri)
    try:
        yield client
    finally:
        client.close()

def save_data_to_db(data, mongo_uri, db_name, collection_name, perform_sentiment_analysis=False):
    """
    Saves data to MongoDB.
    Uses the context manager `get_mongo_client` to handle the client connection.
    Optionally, the data can be analyzed for sentiment before saving.
    If the `perform_sentiment_analysis` flag is set to `True`, the sentiment is calculated.
    Sentiment analysis is done using the `analyse_sentiment` function from `analyse_sentiment.py`.
    """
    with get_mongo_client(mongo_uri) as client:
        db = client[db_name]
        collection = db[collection_name]

        # Create a unique index on 'url' if it doesn't already exist to avoid duplicates
        collection.create_index("url", unique=True)

        # Insert news data with duplicate checking
        new_articles = 0
        for article in data:
            if perform_sentiment_analysis and 'content' in article:
                article['sentiment'] = analyse_sentiment(article['content'])

            try:
                result = collection.update_one(
                    {"url": article['url']},  # Condition to find the document
                    {"$setOnInsert": article},  # Operation if the document is not found
                    upsert=True  # Insert a new document if one doesn't exist
                )
                if result.upserted_id:
                    new_articles += 1
            except Exception as e:
                print(f"Failed to insert/update article {article['url']}: {e}")
        
        print(f"Inserted or updated {new_articles} new articles into {db_name}:{collection_name}")

def get_news_from_db(db_name, collection_name, mongo_uri):
    """
    Gets news data from MongoDB.
    Uses the context manager `get_mongo_client` to handle the client connection.
    """
    with get_mongo_client(mongo_uri) as client:
        db = client[db_name]
        collection = db[collection_name]

        news_articles = list(collection.find({}))
        print(f"Retrieved {len(news_articles)} articles.")
        for article in news_articles:
            if 'sentiment' in article:
                print(f"Sentiment score of article {article['url']}: {article['sentiment']}")
            else:
                print(f"No sentiment score available for article {article['url']}")
        return news_articles

def clear_collection(db_name, collection_name, mongo_uri):
    """
    Clears all articles from a collection in MongoDB.
    Uses the context manager `get_mongo_client` to handle the client connection.
    """
    with get_mongo_client(mongo_uri) as client:
        db = client[db_name]
        collection = db[collection_name]

        collection.delete_many({})  # This deletes all documents in the collection
        print(f"Cleared all articles from {db_name}:{collection_name}")

def delete_article_by_url(url, db_name, collection_name, mongo_uri):
    """
    Deletes an article from a collection in MongoDB based on the URL.
    Uses the context manager `get_mongo_client` to handle the client connection.
    """
    with get_mongo_client(mongo_uri) as client:
        db = client[db_name]
        collection = db[collection_name]

        result = collection.delete_one({"url": url})
        if result.deleted_count > 0:
            print(f"Deleted article with URL {url}")
        else:
            print(f"No article found with URL {url} to delete")
