-- Bougies incohérentes (high trop bas ou low trop haut). Résultat attendu : 0
SELECT COUNT(*) FROM candles WHERE high < open OR high < close OR high < low OR low > open OR low > close;

-- Bougies avec un écart différent de 3 600 000ms (1 heure). Résultat attendu : Une seule ligne : 24/03/2023, bougie de 13:00 UTC manquante.
SELECT * FROM (
    SELECT datetime(open_time / 1000, 'unixepoch') AS heure,
           open_time - LAG(open_time) OVER (ORDER BY open_time) AS ecart
    FROM candles
) WHERE ecart != 3600000;
