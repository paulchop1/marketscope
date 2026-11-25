# MarketScope

Projet d'apprentissage : un testeur de mes règles de trading. Il récupère des bougies historiques, les stocke dans une base SQLite, puis appliquera automatiquement mes définitions (sweeps, cassures de structure) à des centaines de cas, au lieu de la quinzaine que je peux vérifier à la main sur un graphique.

L'objectif est d'obtenir des statistiques fiables, sans biais de sélection ni erreur de lecture à l'œil. Ce n'est ni un bot qui prédit le marché, ni un outil qui passe des ordres.

## État du projet

- ✅ Collecte des bougies 1h de BTCUSDT depuis 2023 (API publique de Binance), mise à jour automatique toutes les heures
- ✅ Contrôles qualité : bougies incohérentes et bougies manquantes
- ⏳ Unités de temps 15m et 1d
- ⏳ Détection des sommets, creux, sweeps et BOS

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python create_db.py
```

## Utilisation

Collecter les bougies (au premier lancement, tout l'historique depuis 2023 ; ensuite, seulement les nouvelles bougies) :

```bash
python fetch_candles.py
```

Le script n'affiche rien dans le Terminal : l'activité et les erreurs sont enregistrées dans `marketscope.log`. Pour voir les dernières lignes, ou uniquement les erreurs :

```bash
tail -n 5 marketscope.log
grep ERROR marketscope.log
```

Lancer les contrôles qualité :

```bash
sqlite3 marketscope.db < controles_qualite.sql
```

Un trou connu existe dans les données de Binance : la bougie 1h du 24/03/2023 à 13:00 UTC n'a jamais été produite (interruption des échanges).

## Automatisation

Ouvrir la crontab avec `EDITOR=nano crontab -e`, puis ajouter cette ligne, en remplaçant `/chemin/vers/marketscope` par le chemin absolu du projet (la commande `pwd`, tapée dans le dossier du projet, l'affiche) :

```
2 * * * * cd /chemin/vers/marketscope && .venv/bin/python fetch_candles.py
```

La collecte est lancée à la minute 2 de chaque heure, pour laisser à Binance le temps de finaliser la bougie qui vient de se clôturer. Elle ne tourne que si l'ordinateur est allumé et éveillé ; au lancement suivant, les bougies manquantes sont récupérées automatiquement.
