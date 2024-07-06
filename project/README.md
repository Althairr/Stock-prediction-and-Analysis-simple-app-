# Stock Prediction and Analysis Dashboard App
>CS50p Final Project

>Video Demo:  [Click This Link](https://www.youtube.com/watch?v=pY-l2xQyqCc)

## Overview 

This project able to help you on providing some insights for users by doing a comprehensive stock prediction and analysis dashboard built using Python and Streamlit. This application provides users with the ability to:
- Predict stock prices,
- Visualize stock data, and
- Analyze sentiment

## Why i build this project

So, the reason why I build this project is actually divided into several reasons:
- I'm interested in data science. So by building this project, i hope my knowledge of the data science, visual, and analysis can be better.
- I want to try something new and because of this project, i feel more empowered to explore the data world.

## Key Features
- **Stock Prediction:** Users can select a stock and predict its future prices for a specified number of years. The predictions are visualized using interactive charts, showing both the forecasted prices and their components.
- **Stock Dashboard:** Displays historical stock data including opening and closing prices. Users can view and interact with the data through dynamic charts.
- **Sentiment Analysis:** Users can select a stock and analyze the sentiment of recent news articles about it. The sentiment scores and labels (positive, negative, neutral) are displayed for each article.

## Technologies Used
Although not all libraries mentioned here, the following technologies that i used for making this project are:

- **Streamlit:** For creating the interactive web application.
- **Prophet:** For time-series forecasting.
- **yFinance:** For fetching historical stock data from Yahoo Finance.
- **Plotly:** For creating interactive plots and charts.
- **VADER Sentiment Analysis:** For performing sentiment analysis on news articles.
- **NewsAPI:** For fetching recent news articles related to the stocks (API key hidden using dotenv).

This application aims to provide stock traders and enthusiasts with a powerful tool to make informed decisions based on both quantitative forecasts and qualitative sentiment analysis.

## Usage
### Stock Prediction
1. Navigate to the "Stock Prediction" section using the navigation bar.
2. Select a stock from the dropdown menu.
3. Choose the number of years to predict using the slider.
4. View the forecasted stock prices and their components.

### Stock Dashboard
1. Navigate to the "Dashboard" section using the navigation bar.
2. View historical stock data including opening and closing prices for various stocks.
3. Interact with the dynamic charts to analyze the data.

### Sentiment Analysis
1. Navigate to the "Sentiment Analysis" section using the navigation bar.
2. Select a stock from the dropdown menu.
3. View the sentiment analysis results for recent news articles about the selected stock.

## More Detailed Information
### How prophet works for stock predictions as far as i know
- Prepare our historical data, ensuring it includes dates and corresponding closing prices. 
- Next, we need to initialize a Prophet model and fit it to our dataset. Prophet then generates a future timeline (future dataframe) based on our specified prediction period. Using this timeline, the model predicts future stock prices and provides uncertainty intervals around these predictions, offering insights into potential price ranges. 
- Finally, Prophet's visualizations help interpret the forecasted trends and adjust the model parameters as needed for better accuracy, ensuring informed decision-making for investors. 

Prophet also automatically identifies changepoints in the data, indicating shifts in trends or abrupt changes in stock prices.

## ACKNOWLEDGEMENTS
I would like to give a very big thank you to my parents who have been there from my childhood until now, even buying me a laptop so that this project can be completed. Also, I would like to express my gratitude to CS50p, Harvard, Staff, and Professor David J. Malan and his team for providing this course.

Thank you very much