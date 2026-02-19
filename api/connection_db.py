import os
import sqlite3

import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wildprint.db")

df = pd.read_csv(os.path.join(BASE_DIR, "infos_especes.csv"), sep=";", encoding="utf-8")

conn = sqlite3.connect(DB_PATH)
df.to_sql("animals", conn, if_exists="replace", index=False)

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tracks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT NOT NULL,
        loc TEXT NOT NULL,
        date DATETIME NOT NULL,
        animal_sp TEXT NOT NULL,
        FOREIGN KEY (animal_sp) REFERENCES animals(species)
    )
""")

conn.commit()
conn.close()
