# Module_13_3

Zadanie: baza danych. 

Skorzystaj z danych clean_stations.csv oraz clean_measure.csv. Na podstawie tych zbiorów stwórz bazę danych i tabelę


Wyjaśnienie:
- pd.read_csv() wczytuje dane z plików CSV do ramki danych Pandas.
- sqlite3.connect('weather_data.db') tworzy połączenie z bazą danych SQLite. Jeśli plik bazy nie istnieje, zostanie utworzony.
- to_sql() zapisuje dane z Pandas DataFrame do tabeli w bazie danych SQLite. Używamy opcji if_exists='replace', aby zastąpić istniejącą tabelę, jeśli taka istnieje.
- Po wykonaniu zapytania SELECT * FROM stations LIMIT 5, wynik jest wypisywany jako lista krotek z pierwszymi 5 rekordami z tabeli stations.