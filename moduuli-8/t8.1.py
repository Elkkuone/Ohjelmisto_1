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
    #poistetaan kaikki muut paitsi a-z krijaimet, A-Z kirjaimet ja 0-9 numerot
    kaunis = re.sub(r"[^a-zA-Z0-9 ]", "",str(ruma))
    return kaunis

print("kerro haluamasi lentokentän ICAO koodi: ")
icao = input()

dbHaku.execute(f"select name from airport where gps_code like '{icao}'")
print(tulos())
