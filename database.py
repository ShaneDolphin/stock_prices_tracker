from sqlalchemy import create_engine
import pandas as pd

def load_data_to_db(df, db_uri):
    engine = create_engine(db_uri)
    df.to_sql('stock_prices', engine, if_exists='replace', index=True)
