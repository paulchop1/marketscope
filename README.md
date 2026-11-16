# MarketScope

Projet d'apprentissage : un script Python qui récupère les prix actuels de Bitcoin, Ethereum et Solana via l'API publique de Binance.
Objectif à terme : collecter automatiquement des données crypto sur plusieurs exchanges et les stocker dans une base de données.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

```bash
python crypto_prices.py
```

Exemple de résultat (les prix changent à chaque exécution) :

```
Prix du BTCUSDT : 64954.01
Prix du ETHUSDT : 1815.61
Prix du SOLUSDT : 71.73
```
