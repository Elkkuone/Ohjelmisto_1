import re
import mysql.connector
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

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
    #poistetaan kaikki muut paitsi a-z krijaimet, A-Z kirjaimet ja 0-9 numerot (^ tarkoittaa säilytä nämä)
    kaunis = re.sub(r"[^a-zA-Z0-9 ]", "",str(ruma))
    return kaunis

print("Kerron lentokenttien etäisyyden kilometreinä: ")
print("Syötä ensimmäisen lentokentän ICAO koodi: ")
kentta1 = input()
print("Syötä toisen lentokentän ICAO koodi: ")
kentta2 = input()

dbHaku.execute(f"select name from airport where gps_code = '{kentta1}'")
kentta1 = tulos()

dbHaku.execute(f"select name from airport where gps_code = '{kentta2}'")
kentta2 = tulos()

geolocator = Nominatim(user_agent="test")

location1 = geolocator.geocode(str(kentta1))
location2 = geolocator.geocode(str(kentta2))

kentta1 = location1.latitude,location1.longitude
kentta2 = location2.latitude,location2.longitude
lopputulos = geodesic(kentta1, kentta2)

print(f"lentokenttien etäisyys on: {lopputulos}")