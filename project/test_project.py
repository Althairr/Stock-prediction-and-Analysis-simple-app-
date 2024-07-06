import os
import pytest
import requests_mock
from datetime import date
from dotenv import load_dotenv
from project import load_data, get_news, sentiment_analysis

# initialize the env of the project
@pytest.fixture
def setup():
    load_dotenv()

# testh the load_data function
def test_load_data():
    ticker = "MSFT"
    START = "2016-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    data = load_data(ticker, START, TODAY)
    
    assert not data.empty
    assert 'Date' in data.columns
    assert 'Close' in data.columns

# test get_news with mock requests
def test_get_news(setup, requests_mock):
    stock = "AAPL"
    api_key = os.getenv('NEWS_API_KEY')
    url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={api_key}"

    mock_response = {
        "articles": [
            {"title": "Apple stock rises"},
            {"title": "Apple releases new product"}
        ]
    }
    requests_mock.get(url, json=mock_response)
    
    news = get_news(stock)
    assert len(news) == 2
    assert news[0]["title"] == "Apple stock rises"

# test the sentiment analysis function
def test_sentiment_analysis():
    news = [
        {"title": "Apple stock rises"},
        {"title": "Apple faces lawsuit"}
    ]
    
    sentiments = sentiment_analysis(news)
    assert len(sentiments) == 2
    assert sentiments[0]["sentiment"] == "Positive" or sentiments[0]["sentiment"] == "Neutral"
    assert sentiments[1]["sentiment"] == "Negative" or sentiments[1]["sentiment"] == "Neutral"