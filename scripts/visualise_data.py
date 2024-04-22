import matplotlib.pyplot as plt
import pandas as pd
from mongo_utils import get_mongo_client

def plot_sentiment_over_time(db_name, collection_name, mongo_uri):
    """
    Plots the sentiment score over time.
    Uses the context manager `get_mongo_client` to handle the client connection.
    """
    with get_mongo_client(mongo_uri) as client:
        db = client[db_name]
        collection = db[collection_name]
        data = pd.DataFrame(list(collection.find({}, {'publishedAt': 1, 'sentiment': 1})))
        data['publishedAt'] = pd.to_datetime(data['publishedAt'])
        data.sort_values('publishedAt', inplace=True)
        plt.figure(figsize=(10, 6))
        plt.plot(data['publishedAt'], data['sentiment'], marker='o', linestyle='-')
        plt.title('Sentiment Score Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sentiment Score')
        plt.grid(True)
        plt.show()


