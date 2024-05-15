# Stock Price Tracker and Anomaly Detection

This project provides a stock price tracker that ingests stock price data, loads it into a PostgreSQL database, and detects abnormalities in the price changes using machine learning techniques.

## Features

- Fetch stock price data from Alpha Vantage API.
- Load data into a PostgreSQL database.
- Detect anomalies in stock prices using Isolation Forest.
- Visualize stock price data and anomalies.

## Requirements

- Python 3.8+
- PostgreSQL
- Alpha Vantage API key

## Installation

1. Clone the repository:
   ```
   bash
   git clone https://github.com/ShaneDolphin/stock_prices_tracker.git
   cd stock_prices_tracker
   ```
   
2. Install the required Python packages

```
   pip install -r requirements.txt
```

3. Setup up your PostgreSQL database and update the connection string in your **config.py** file.

## Now you're going to want to use this, eh?

1. Get your stock price data. In this case I'm using Apple (AAPL) but you can grab anything.

```
   from data_ingestion import fetch_stock_data

   api_key = 'your_api_key'
   symbol = 'AAPL'
   stock_data = fetch_stock_data(symbol, api_key)
   print(stock_data.head())
```

2. Load this data into your PostgreSQL database
   
```
   from database import load_data_to_db
   from config import DATABASE_URI

   load_data_to_db(stock_data, DATABASE_URI)
```

3. Time to dig deep for those conspiracy theories. Did I say that? I meant anomaly tracking.

```
from anomaly_detection import detect_anomalies, plot_anomalies

anomaly_data = detect_anomalies(stock_data)
plot_anomalies(anomaly_data)
```


