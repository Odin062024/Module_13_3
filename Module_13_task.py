import sqlite3
import pandas as pd

stations_df = pd.read_csv('clean_stations.csv')
measurements_df = pd.read_csv('clean_measure.csv')

conn = sqlite3.connect('clean_data.db')

stations_df.to_sql('stations', conn, if_exists='replace', index=False)
measurements_df.to_sql('measurements', conn, if_exists='replace', index=False)

result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()
print(result)

conn.close()
