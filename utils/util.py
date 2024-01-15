# utils.py

from .util import setup_logger, get_soup_sel
import pandas as pd
import os.path
import sqlite3 as sql


def to_sqlite3(df: pd.core.frame.DataFrame, filename_db: str, tablename: str):
    conn = sql.connect(filename_db)
    # Write the new DataFrame to a new SQLite3 table
    df.to_sql(tablename, conn, if_exists='replace')
    conn.close()
    return None

def csv_to_df(filename: str) -> pd.core.frame.DataFrame:
    return pd.read_csv(filename)

def view_db(dbname: str, tablename: str) -> list:
    new_data = sql.connect(dbname)
    change = new_data.cursor()
    change.execute(f"SELECT * FROM {tablename}")
    rows = change.fetchall()
    change.close()
    return rows


