import re

print(" anna lukuja, lasken ne yhteen: laita merkki v kun olet valmis laskemaan luvut yhteen")
luvut = []
parilliset = []
def laskuri(kaikki,luvut, parilliset):
    kaikki = sum(luvut)
    #haluan kaikki parilliset luvut, joten pitää saada parittomat pois
    #luku on pariton, jos sitä ei pysty jakamaan kahdella
    for i in range(len(luvut)):
        if luvut[i] % 2 == 0:
            parilliset.append(luvut[i])
    return kaikki,parilliset

while True:
    luku = input()
    if luku == "v":
        lopputulos = str((laskuri(None, luvut, [])))
        lopputulos = lopputulos.replace(")","").replace("(","").replace(",","")
#        lopputulos = lopputulos[:] + " ja parillisia:" + lopputulos[:]
        print("Lukuja on yhteensä ja parillisia: " + str(lopputulos))
        break
    list.append(luvut,int(luku))
