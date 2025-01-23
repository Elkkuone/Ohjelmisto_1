print("hei käyttäjä, voit antaa lukuja niin kauaan kuin haluat, sulkeaksesi jätä välilyönti ja saat pienimmän ja suurinmman syötetyn luvun")
#nyt 0 laittaminen ei enää resettaa lukuja
pienin = float()
suurin = float()
while True:
    luku = (input())
    if luku == str(" "):
        print("suurin luku on " + str((pienin)))
        print("pienin luku on " + str((suurin)))
        break
    else:
        luku = float(luku)
        if pienin == None:
            pienin = luku
        if suurin == None:
            suurin = luku
        if luku < suurin:
            suurin = luku
        if luku > pienin:
            pienin = luku
