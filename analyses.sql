-- Les 5 derniers prix du BTC, du plus récent au plus ancien
SELECT * FROM prices WHERE symbol = 'BTCUSDT' ORDER BY timestamp DESC LIMIT 5;

-- Le prix le plus bas du SOL enregistré, avec son heure
SELECT timestamp, price FROM prices WHERE symbol = 'SOLUSDT' ORDER BY price LIMIT 1;

-- Le nombre de relevés, le prix minimum, le prix maximum, le prix moyen, arrondi à 2 décimales de chaque crypto
SELECT symbol, COUNT(*) AS nb_releves, MIN(price) AS prix_min, MAX(price) AS prix_max, ROUND(AVG(price), 2) AS prix_moyen FROM prices GROUP BY symbol;
