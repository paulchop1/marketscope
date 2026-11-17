# MarketScope

Projet d'apprentissage : un collecteur Python qui récupère toutes les minutes les prix de Bitcoin, Ethereum et Solana via l'API publique de Binance, et les enregistre avec leur heure de relevé dans une base de données SQLite..
Objectif à terme : collecter des données crypto sur plusieurs exchanges.

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

Le script n’affiche rien dans le Terminal, les prix sont enregistrés dans la base et l’activité dans `marketscope.log`.

Extrait du journal :

```
2026-11-17 21:49:01,049 INFO BTCUSDT : 63918.71
2026-11-17 21:49:01,349 INFO ETHUSDT : 1796.87
2026-11-17 21:49:01,660 INFO SOLUSDT : 72.89
```

Pour consulter les prix enregistrés dans la base : 

```bash
sqlite3 marketscope.db "SELECT * FROM prices;"
```

## Automatisation

Ouvrir la crontab : 
```bash 
EDITOR=nano crontab -e
```

Ajouter cette ligne, qui lance le collecteur toutes les minutes :

```
* * * * * cd /chemin/vers/marketscope && .venv/bin/python crypto_prices.py
```

Remplacez `/chemin/vers/marketscope` par le chemin absolu de votre dossier.

Astuce : la commande `pwd`, tapée dans le dossier du projet, affiche ce chemin.


Enregistrer avec **Ctrl + O** puis **Entrée**, puis quitter avec **Ctrl + X**.

L’activité et les erreurs sont enregistrées dans `marketscope.log`.

Pour afficher les dernières lignes du fichier (remplacer 9 par le nombre de lignes souhaité) : 

```bash
tail -n 9 marketscope.log
```

Pour voir uniquement les erreurs : 

```bash
grep ERROR marketscope.log
```

Le collecteur ne tourne que si l’ordinateur est allumé et pas en veille. 

Comment l’arrêter ? Rouvrir la crontab et supprimer la ligne ou mettre un `#` devant.
