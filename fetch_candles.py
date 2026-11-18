import requests                              # pour interroger l'API de Binance
import sqlite3                               # pour écrire dans la base
import time                                  # pour l'heure actuelle et les pauses
from datetime import datetime, timezone      # pour fabriquer une date de départ

SYMBOLE = "BTCUSDT"                          # l'actif à collecter
INTERVALLE = "1h"                            # l'unité de temps
# date de départ : 1er janvier 2023 à 00:00 UTC, convertie en millisecondes
debut = int(datetime(2023, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)

maintenant = int(time.time() * 1000)         # heure actuelle en millisecondes

connexion = sqlite3.connect("marketscope.db")
requete = """INSERT OR IGNORE INTO candles
    (symbol, interval, open_time, open, high, low, close, volume, close_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

while True:                                  # une page par tour, jusqu'au break
    url = f"https://api.binance.com/api/v3/klines?symbol={SYMBOLE}&interval={INTERVALLE}&limit=1000&startTime={debut}"
    reponse = requests.get(url, timeout=10)  # envoie la requête, 10 s maximum
    reponse.raise_for_status()               # erreur si code 4xx ou 5xx
    bougies = reponse.json()                 # jusqu'à 1000 bougies à partir de "debut"

    if len(bougies) == 0:                    # plus aucune bougie : on a tout récupéré
        break

    for bougie in bougies:
        if bougie[6] < maintenant:           # seulement les bougies clôturées
            connexion.execute(requete, (
                SYMBOLE, INTERVALLE, bougie[0],
                float(bougie[1]), float(bougie[2]), float(bougie[3]),
                float(bougie[4]), float(bougie[5]), bougie[6],
            ))
    connexion.commit()                       # on valide à chaque page

    print(f"Page reçue : {len(bougies)} bougies, total ajouté : {connexion.total_changes}")

    if len(bougies) < 1000:                  # page incomplète : on est arrivé au présent
        break

    debut = bougies[-1][6] + 1               # prochaine page : juste après la clôture de la dernière bougie
    time.sleep(0.5)                          # pause pour ne pas surcharger Binance

connexion.close()
print("Collecte terminée")
