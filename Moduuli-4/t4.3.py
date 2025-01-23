


print("hei käyttäjä, voit antaa lukuja niin kauaan kuin haluat, sulkeaksesi jätä välilyönti ja saat pienimmän ja suurinmman syötetyn luvun")
i = True
pienin = 0
suurin = 0
while i:
    luku = (input())
    if luku == str(" "):
        print("suurin luku on " + str((pienin)))
        print("pienin luku on " + str((suurin)))
        break
    else:
        luku = float(luku)
        if pienin == 0:
            pienin = luku
        if suurin == 0:
            suurin = luku
        if luku < suurin:
            suurin = luku
        if luku > pienin:
            pienin = luku
