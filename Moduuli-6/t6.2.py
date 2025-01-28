import random


print("hei, ilmoita suurin nopan silmämäärä: ")
heitot = []
suurinluku = int(input())

def noppa(heitto,suurinluku):
    heitto= random.randint(1, int(suurinluku))
    list.append(heitot,heitto)
    return heitto

noppa(None,suurinluku)



while True:
    heitto = noppa(None,suurinluku)
    if heitto == suurinluku:
        print(f"Nopasta tuli {heitto} onneksi olkoon! Yhteensä noppaheitoista tuli {sum(heitot)}")
        break
    else:
        print(f"Nopasta tuli {heitto} voi harmi!")
