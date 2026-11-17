import requests 
from datetime import datetime, timezone
import sqlite3
import logging
logging.basicConfig(
    filename="marketscope.log",                        
    level=logging.INFO,                                
    format="%(asctime)s %(levelname)s %(message)s",
) 
connexion = sqlite3.connect("marketscope.db")
requete = "INSERT INTO prices (timestamp, exchange, symbol, price) VALUES (?, ?, ?, ?)"
symboles = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
for crypto in symboles:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}"
    try : 
        reponse = requests.get(url, timeout=10)
        reponse.raise_for_status() 
    except requests.exceptions.RequestException as erreur :
        logging.error(f"Erreur pour {crypto} : {erreur} ")
        continue
    donnees = reponse.json()
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prix = float(donnees["price"])
    connexion.execute(requete, (timestamp, "binance", crypto, prix))
    logging.info(f"{crypto} : {prix}")
connexion.commit()
connexion.close()
