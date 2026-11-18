# MarketScope

Projet d'apprentissage : un testeur de mes règles de trading. Il récupère des bougies historiques, les stocke dans une base SQLite, puis applique automatiquement mes définitions (sweeps, cassures de structure) à des centaines de cas, au lieu de la quinzaine que je peux vérifier à la main sur un graphique.

L'objectif est d'obtenir des statistiques fiables, sans biais de sélection ni erreur de lecture à l'œil. Ce n'est ni un bot qui prédit le marché, ni un outil qui passe des ordres.

## État du projet

En construction. Étape actuelle : collecte des bougies 1h de BTCUSDT depuis l'API publique de Binance.

## Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
