import requests
import pandas as pd

def fetch_stock_data(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df.columns = [col.split(' ')[1] for col in df.columns]
    df.index = pd.to_datetime(df.index)
    return df