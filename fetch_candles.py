import requests
import sqlite3
import time
from datetime import datetime, timezone
import logging

logging.basicConfig(
    filename="marketscope.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

SYMBOLE = "BTCUSDT"
INTERVALLE = "1h"
DUREES = {"15m": 900000, "1h": 3600000, "1d": 86400000}

maintenant = int(time.time() * 1000)

connexion = sqlite3.connect("marketscope.db")
requete = """INSERT OR IGNORE INTO candles
    (symbol, interval, open_time, open, high, low, close, volume, close_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

requete_max = "SELECT MAX(open_time) FROM candles WHERE symbol = ? AND interval = ?"
resultat = connexion.execute(requete_max, (SYMBOLE, INTERVALLE)).fetchone()
if resultat[0] is None:
    debut = int(datetime(2023, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
else:
    debut = resultat[0] + DUREES [INTERVALLE]

while True:
    url = f"https://api.binance.com/api/v3/klines?symbol={SYMBOLE}&interval={INTERVALLE}&limit=1000&startTime={debut}"
    try:
        reponse = requests.get(url, timeout=10)
        reponse.raise_for_status()
    except requests.exceptions.RequestException as erreur:
        logging.error(f"Collecte {SYMBOLE} {INTERVALLE} interrompue : {erreur}")
        break
    bougies = reponse.json()

    if len(bougies) == 0:
        break

    for bougie in bougies:
        if bougie[6] < maintenant:
            connexion.execute(requete, (
                SYMBOLE, INTERVALLE, bougie[0],
                float(bougie[1]), float(bougie[2]), float(bougie[3]),
                float(bougie[4]), float(bougie[5]), bougie[6],
            ))
    connexion.commit()

    logging.info(f"Page reçue : {len(bougies)} bougies, total ajouté : {connexion.total_changes}")

    if len(bougies) < 1000:
        break

    debut = bougies[-1][6] + 1
    time.sleep(0.5)

connexion.close()
logging.info("Collecte terminée")

