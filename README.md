# Predicting stock prices based on news sentiment analysis. 

This project blends fetching dynamic data from the internet with a manageable scope of predictive modeling.

# Project high level overview

Goal: Develop a model to predict stock price changes based on the sentiment derived from financial news headlines. This involves fetching news dynamically, performing sentiment analysis, and correlating these sentiments with stock price movements.

## High level steps
1. Data Collection:
Stock Price Data: Use APIs like Alpha Vantage, Yahoo Finance, or similar services that provide historical stock prices.
News Headlines: Fetch financial news headlines dynamically using news APIs like NewsAPI or web scraping techniques targeting financial news websites.

2. Data Processing:
Sentiment Analysis: Use natural language processing (NLP) libraries like NLTK or spaCy to analyze the sentiment of each news headline. Classify sentiments as positive, negative, or neutral.
Data Aggregation: Aggregate sentiments by day and match these with daily stock price movements. Calculate the daily sentiment score and correlate it with stock price changes.

3. Exploratory Data Analysis (EDA):
Visualise Data: Use matplotlib or seaborn to visualise relationships between sentiment scores and stock price changes.
Feature Engineering: Create features such as moving averages of sentiment scores or lag features that may influence stock prices.

4. Model Development:
Model Selection: Choose machine learning models suitable for regression or classification (depending on specific prediction goal). Start with simpler models like linear regression and  move to more complex models like Random Forest or LSTM (Long Short-Term Memory networks) if necessary.
Training and Validation: Train models using the historical data and validate using techniques like k-fold cross-validation.

5. Model Evaluation and Tuning:
Performance Metrics: Use metrics like MSE (Mean Squared Error) for regression tasks or accuracy and F1-score for classification tasks.
Parameter Tuning: Use grid search or random search to fine-tune your model parameters to improve performance.

6. Deployment:
Web Application: Build a simple Flask or Django app that fetches new news headlines, predicts the sentiment, and displays predicted stock price movements.
Dashboard: Use Plotly Dash to create interactive dashboards to display real-time analysis and predictions.


## Tools and Libraries I might need
- Python: For all scripting and model development.
- Pandas & NumPy: For data manipulation.
- NLTK/spaCy: For natural language processing.
- Scikit-Learn, Keras, or TensorFlow: For building and training predictive models.
- Matplotlib/Seaborn/Plotly: For data visualization.
- Flask/Django: For deploying a web application.
- SQL/NoSQL: For data storage if needed.

# BACKLOG

## In progress 
- Start visualise_data.py with a function to plot sentiment over time

## Next up
- Document docker and mongodb setup
- Collectin and integration of stock prices
- Narrow news article fetching and stock price fetchig (e.g., tech articles and tech stocks)

## To do

- Stock price fetching
    - Generalise or add to fetch_news.py

- Data Aggregation
    - Aggregate sentiments by day and match these with daily stock price movements. Calculate the daily sentiment score and correlate it with stock price changes.

- EDA
    - Visualise data using matplotlib/seaborn to visualise relationships between sentiment and price changes
    - Feature engineering like moving averages of sentiment scores or lag features that may influence stock prices

- Model development
    - model selection for regression or classification depending on prediction goal
    - Start with linear regression
    - Consider other models (Random Forest or LSTM)

- Training and Validation
    - Train models with historical data
    - Validate using techniques like k-fold cross-validation

- Model evaluation and tuning
    - Performance metrics like MSE (for regression) and F1-score (for classification)
    - Parameter tuning using grid search or random search to fine-tune model parameters to improve performance

- Deployment
    - Web App build via Flask or Django that fetches new news headlines, predicts the sentiment, and displays predict stock price movements
    - Dashboard via Plotly Dash to create interactive dashbboards to display real-time analysis and predictions

## Done
- News fetching via fetch_news.py
- Sentiment analysis of news via analyse_sentiment.py
- News saving via mongo_utils.py

# SETUP

## .env

```
NEWS_API_KEY=1d6b660bec584a85b9f9bdda38ec449b
MONGO_URI=mongodb://localhost:27017/
DB_NAME=newsDatabase
COLLECTION_NAME=articles
```

## venv

Uses a `venv` to manage dependencies

## Mongo DB
- Start docker

- Pull the mongo DB image from Docker Hub (unless it has a `stop unless restart` policy, then the container will start as soon as Docker is launched)

    ```
    docker pull mongo # run from /data/mongo_data)
    ```
     
- Run the MongoDB container (only if it won't start automatically with docker)

    ```
    docker run --name mongodb -v ~/repos/sentiment-stock-prediction/data/mongo_data:/data/db -p 27017:27017 -d --restart unless-stopped mongo
    ```

- Verify the data volume is mounted in the container 

    ```
    docker inspect -f '{{ .Mounts }}' <container-ID>
    ```