# MarketScope

Projet d'apprentissage : un script Python qui récupère et enregistre dans une base de données SQLite les prix et les heures de relevé de Bitcoin, Ethereum et Solana via l'API publique de Binance.
Objectif à terme : collecter automatiquement des données crypto sur plusieurs exchanges.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python create_db.py
```

## Utilisation

```bash
python crypto_prices.py
```

Exemple de résultat (les prix et la date changent à chaque exécution) :

```
2026-11-16T21:48:54Z | BTCUSDT : 65323.39
2026-11-16T21:48:55Z | ETHUSDT : 1829.05
2026-11-16T21:48:55Z | SOLUSDT : 71.97
```

Pour consulter les prix enregistrés dans la base : 

```bash
sqlite3 marketscope.db "SELECT * FROM prices;"
```
