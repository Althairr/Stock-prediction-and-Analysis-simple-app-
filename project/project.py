# import libraries
import os
import streamlit as st
from datetime import date
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as graph
from streamlit_navigation_bar import st_navbar
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dotenv import load_dotenv

def main():
    # display the navbar for the user to choose
    page = st_navbar(["Stock Prediction", "Dashboard", "Sentiment Analysis"])

    # Dictionary for storing the navbar
    functions = {
        "Stock Prediction": show_home,
        "Dashboard": show_dashboard,
        "Sentiment Analysis": show_news,
    }

    # get the navbar based on the function picked
    go_to = functions.get(page)
    if go_to:
        go_to()

def show_home():
    # initialize 
    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    # initialize variables
    stocks = ["AAPL", "GOOG", "MSFT", "TSLA", "GME"]

    # display the stock for user to select from
    st.title("Stock Prediction")
    selected_stocks = st.selectbox("Select dataset for prediction", stocks)

    # user will select the years to predict
    n_years = st.slider("Number of years to predict: ", 1, 4)
    period = n_years * 365

    # get the data and load it
    data_load_state = st.text("Loading data...")
    data = load_data(selected_stocks, START, TODAY)
    data_load_state.text("Loading data...done!")

    # perform the forecasting prediction
    forecasting_data(data, period)

def forecasting_data(data, period):
    # select the 'Date' and 'Close' columns from the data
    # and rename the columns to 'ds' (Date) and 'y' (value) as required by Prophet
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    # initialize the Prophet model and fit the model on the training dataset
    m = Prophet()
    m.fit(df_train)
    
    # create a dataframe for future predictions for the specified period and predict it with Prophet
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # display the forecast subheader
    st.subheader("Forecast")
    
    # display the last few rows of the forecast dataframe
    st.write(forecast.tail())

    # plot the forecast data
    st.write('Forecast Data')
    fig1 = plot_plotly(m, forecast)
    
    # display the plot 
    st.plotly_chart(fig1)

    # plot the forecast components (trend, seasonality, etc.) and display it
    st.write('Forecast Components')
    fig2 = m.plot_components(forecast)
    st.write(fig2)


def show_dashboard():
    st.title("Stock Dashboard")

    # initialize 
    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    # defining ticker variables
    aapl = "AAPL"
    goog = "GOOG"
    msft = "MSFT"
    tsla = "TSLA"
    gme = "GME"

    # get the data from yfinance
    aapl_data = yf.Ticker(aapl)
    goog_data = yf.Ticker(goog)
    msft_data = yf.Ticker(msft)
    tsla_data = yf.Ticker(tsla)
    gme_data = yf.Ticker(gme)

    # fetch history data from yfinance
    aapl_hist = aapl_data.history(period= "max")
    goog_hist = goog_data.history(period="max")
    msft_hist = msft_data.history(period="max")
    tsla_hist = tsla_data.history(period="max")
    gme_hist = gme_data.history(period="max")

    # fetch the stock data for the dataframe
    aapl_stock = load_data(aapl, START, TODAY)
    goog_stock = load_data(goog, START, TODAY)
    msft_stock = load_data(msft, START, TODAY)
    tsla_stock = load_data(tsla, START, TODAY)
    gme_stock = load_data(gme, START, TODAY)

    # AAPL's stock
    st.subheader("AAPL's stock")
    st.write(aapl_stock.tail())

    # display the closing price
    st.write("AAPL's Closing Price")
    st.bar_chart(aapl_hist.Close)
    plot_raw_data(aapl_stock)

    # GOOG's stock
    st.subheader("GOOG's stock")
    st.write(goog_stock.tail())

    # display the closing price
    st.write("GOOG's Closing Price")
    st.bar_chart(goog_hist.Close)
    plot_raw_data(goog_stock)

    # MSFT's stock
    st.subheader("MSFT's stock")
    st.write(msft_stock.tail())

    # display the closing price
    st.write("MSFT's Closing Price")
    st.bar_chart(msft_hist.Close)
    plot_raw_data(msft_stock)

    # TSLA's stock
    st.subheader("TSLA's stock")
    st.write(tsla_stock.tail())

    # display the closing price
    st.write("TSLA's Closing Price")
    st.bar_chart(tsla_hist.Close)
    plot_raw_data(tsla_stock)

    # GME's stock
    st.subheader("GME's stock")
    st.write(gme_stock.tail())

    # display the closing price
    st.write("GME's Closing Price")
    st.bar_chart(gme_hist.Close)
    plot_raw_data(gme_stock)

@st.cache_data
def load_data(ticker, START, TODAY):
    # download the ticker data from yfinance
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

def plot_raw_data(data):
    # create a new figure object
    fig = graph.Figure()

    # add a trace for the stock's opening price and the closing price
    fig.add_trace(graph.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(graph.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))

    # update the layout and display it 
    fig.layout.update(title_text="Time series data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

def show_news():
    # initialize the stocks
    stocks = ["AAPL", "GOOG", "MSFT", "TSLA", "GME"]
    
    # display the title
    st.title("Sentiment Analysis")

    # Create a select box for the user to choose a stock to analyze
    selected_stock = st.selectbox("Select dataset to analyze", stocks)
    
    # Fetch news articles related to the selected stock
    news = get_news(selected_stock)
    
    # Perform sentiment analysis on the fetched news articles
    sentiments = sentiment_analysis(news)
    
    # Display the sentiments analysis results for the selected stock
    st.write(f"Sentiments for recent news about {selected_stock}:")
    st.write(sentiments)

# get the news from the newsapi
def get_news(stock):
    load_dotenv()
    api_key = os.getenv('NEWS_API_KEY')
    url = f"https://newsapi.org/v2/everything?q={stock}&apiKey={api_key}"
    response = requests.get(url)
    return response.json()["articles"]

def sentiment_analysis(news):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = []
    
    for article in news:
        score = analyzer.polarity_scores(article["title"])
        
        # Determine sentiment as positive, negative, or neutral
        if score['compound'] >= 0.05:
            sentiment_label = "Positive"
        elif score['compound'] <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"
        
        # Add sentiment to the list
        sentiments.append({
            "title": article["title"],
            "score": score,
            "sentiment": sentiment_label
        })
    
    # return the list of articles
    return sentiments


if __name__ == '__main__':
    main()
