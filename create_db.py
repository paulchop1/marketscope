import sqlite3
connexion = sqlite3.connect("marketscope.db")
requete = """
CREATE TABLE IF NOT EXISTS prices (
    timestamp TEXT NOT NULL,
    exchange  TEXT NOT NULL,
    symbol    TEXT NOT NULL,
    price     REAL NOT NULL
);
"""
connexion.execute(requete)
connexion.commit()
connexion.close()
print("Table créée")
