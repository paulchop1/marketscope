import sqlite3
connexion = sqlite3.connect("marketscope.db")
requete = """
CREATE TABLE IF NOT EXISTS candles (
    symbol TEXT NOT NULL,
    interval  TEXT NOT NULL,
    open_time    INTEGER NOT NULL,
    open     REAL NOT NULL,
    high     REAL NOT NULL,
    low        REAL NOT NULL,
    close      REAL NOT NULL,
    volume      REAL NOT NULL,
    close_time     INTEGER NOT NULL,
    PRIMARY KEY (symbol, interval, open_time)
);
"""
connexion.execute(requete)
connexion.commit()
connexion.close()
print("Table créée")
