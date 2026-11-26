-- Bougies dont l'écart avec la précédente (dans la même UT) diffère de la durée de l'UT.
-- Résultat attendu : uniquement des trous connus (ex. 24/03/2023 vers 13:00 UTC en 15m et 1h).
SELECT * FROM (
    SELECT interval,                                                    -- ← modif. 1 : juste la colonne, rien d'autre
           datetime(open_time / 1000, 'unixepoch') AS heure,            -- inchangée
           open_time - LAG(open_time) OVER (PARTITION BY interval ORDER BY open_time) AS ecart   -- ← modif. 2
    FROM candles
) WHERE ecart != CASE interval WHEN '15m' THEN 900000 WHEN '1h' THEN 3600000 WHEN '1d' THEN 86400000 END;   -- ← modif. 3
