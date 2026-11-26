import sqlite3
import pandas as pd

connexion = sqlite3.connect("marketscope.db")

texte_sql = "SELECT * FROM candles WHERE interval = '1d'"

df = pd.read_sql_query(texte_sql, connexion)

connexion.close()

df["date"] = pd.to_datetime(df["open_time"], unit="ms", utc=True)
df["variation"] = ((df["close"] - df["open"]) / df["open"]) * 100
print(df.shape)
print(df[["date", "open", "close", "variation"]].head())
print(df["variation"].describe())
