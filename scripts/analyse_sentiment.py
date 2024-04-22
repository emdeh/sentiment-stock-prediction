from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

def analyse_sentiment(text):
    """
    This function is used to analyze the sentiment of the news articles.
    It is called in the `save_data_to_db` function in `mongo_utils.py`.
    It is called if the `perform_sentiment_analysis` flag is set to `True`.
    """
    sid = SentimentIntensityAnalyzer()
    return sid.polarity_scores(text)['compound']