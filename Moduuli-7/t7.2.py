print("syötä nimiä, lopussa saat tiedon onko viimeisin nimi uusi vai vanha ja kaikki syötetyt sekaisessa järjestyksessä: ")
nimilista = set()
while True:
    nimi = input()
    if nimi == "":
        #tehdään nimistä nätinpiä:
        lopputulos = str(nimilista).replace("{","").replace("}","")
        print(" tässä kaikki nimesi : " + lopputulos)
        break
    if nimi in nimilista:
        print("Aiemmin syötetty nimi ")
    else:
        print ("Uusi nimi ")
    nimilista.add(nimi)