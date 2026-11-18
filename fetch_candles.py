import requests                      
import sqlite3
import time                                                                    
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000"
reponse = requests.get(url, timeout=10)     
reponse.raise_for_status()                  
bougies = reponse.json()                   

maintenant = int(time.time() * 1000)        

connexion = sqlite3.connect("marketscope.db")

requete = """INSERT OR IGNORE INTO candles
    (symbol, interval, open_time, open, high, low, close, volume, close_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

for bougie in bougies:                      
    if bougie[6] < maintenant:             
        connexion.execute(requete, (
            "BTCUSDT",                      
            "1h",                           
            bougie[0],                    
            float(bougie[1]),               
            float(bougie[2]),               
            float(bougie[3]),             
            float(bougie[4]),           
            float(bougie[5]),              
            bougie[6],                      
        ))

connexion.commit()                          
print(f"Bougies ajoutées : {connexion.total_changes}")   
connexion.close()
