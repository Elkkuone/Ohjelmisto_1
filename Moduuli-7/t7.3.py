import mysql.connector


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
  var = dbHaku.fetchall()
  return var

dbHaku.execute("use flight_game")
dbHaku.execute("select * from game")
print(tulos())
