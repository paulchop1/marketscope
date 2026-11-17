import requests 
from datetime import datetime, timezone
import sqlite3
connexion = sqlite3.connect("marketscope.db")
requete = "INSERT INTO prices (timestamp, exchange, symbol, price) VALUES (?, ?, ?, ?)"
symboles = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
for crypto in symboles:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}"
    try : 
        reponse = requests.get(url, timeout=10)
        reponse.raise_for_status() 
    except requests.exceptions.RequestException as erreur :
        print(f"Erreur pour {crypto} : {erreur} ")
        continue
    donnees = reponse.json()
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prix = float(donnees["price"])
    connexion.execute(requete, (timestamp, "binance", crypto, prix))
    print(f"{timestamp} | {crypto} : {prix}")
connexion.commit()
connexion.close()
