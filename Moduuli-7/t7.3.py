lentokentat = {}

while True:
  print("Haluatko syöttää uuden lentoaseman (syötä 1) vai hakea jo syötetyn? (syötä 2) vai lopettaa (syötä 3) ")
  valinta = int(input())
  if valinta == 1:
    print("syötä ICAO-koodi: ")
    icao = input()
    print("syötä lentokentän nimi: ")
    nimi = input()
    lentokentat.update({icao: nimi})
  if valinta == 2:
    print(" anna ICAO-koodi: ")
    icao = input()
    if icao in lentokentat:
      print("kentän nimi on " + lentokentat[icao])
    else:
      print("Et ole tallentanut tätä aijemmin tai kirjoitit väärin")
  if valinta == 3:
    print("Mukavaa päivää! ")
    break

