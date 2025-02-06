from idlelib.replace import replace

import mysql.connector
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="Eelis",
  password="OlenKoulussa",
  database="flight_game"
)

#tehdään hakuväline databaseen selvemmäksi
dbHaku = mydb.cursor()

#tehdään databasesta lukeminen selvemmäksi:
def tulos():
    ruma = dbHaku.fetchall()
    kaunis = re.sub(r"[()']", "",str(ruma))
    return kaunis

print("kerro maakoodi niin kerron lentokenttien määrät")
mk = str(input())

dbHaku.execute(f"""
select type, count(*)
from airport 
where iso_country = '{mk}'
group by type desc
;

"""
)

print(f"maakoodilla {mk} löytyy {tulos()} ")
