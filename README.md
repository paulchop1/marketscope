# MarketScope

Projet d'apprentissage : un script Python qui récupère le prix actuel du BTC via l'API publique de Binance.
Objectif à terme : collecter automatiquement des données crypto sur plusieurs exchanges et les stocker dans une base de données.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Utilisation

```bash
python btc_price.py
```

Exemple de résultat (le prix change à chaque exécution) :

```
Prix du BTC : 64850.01 USDT
```