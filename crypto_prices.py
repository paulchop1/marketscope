import requests 
from datetime import datetime, timezone
import sqlite3
connexion = sqlite3.connect("marketscope.db")
requete = "INSERT INTO prices (timestamp, exchange, symbol, price) VALUES (?, ?, ?, ?)"
symboles = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
for crypto in symboles:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}"
    reponse = requests.get(url)
    donnees = reponse.json()
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prix = float(donnees["price"])
    connexion.execute(requete, (timestamp, "binance", crypto, prix))
    print(f"{timestamp} | {crypto} : {prix}")
connexion.commit()
connexion.close()
