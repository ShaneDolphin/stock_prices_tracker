import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest(contamination=0.01)
    df['price_change'] = df['close'].pct_change()
    df.dropna(inplace=True)
    df['anomaly'] = model.fit_predict(df[['price_change']])
    return df

def plot_anomalies(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df.index, y='close', data=df, label='Close Price')
    sns.scatterplot(x=df.index, y='close', data=df[df['anomaly'] == -1], color='red', label='Anomaly')
    plt.title('Stock Price Anomalies')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()
