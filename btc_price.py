import requests 
symboles = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]
for crypto in symboles:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={crypto}"
    reponse = requests.get(url)
    donnees = reponse.json()
    prix = float(donnees["price"])
    print(f"Prix du {crypto} : {prix}")
