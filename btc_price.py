import requests 
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
reponse = requests.get(url)
print(reponse.status_code)
donnees = reponse.json()
prix = float(donnees["price"])
print(f"Prix du BTC : {prix} USDT ")