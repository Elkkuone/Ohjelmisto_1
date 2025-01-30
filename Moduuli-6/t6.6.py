import math


def laskuri(halkaisia,raha):
    # pinta ala cm muodossa
    pala = math.pi * halkaisia ** 2
    # senttimetreistä neliösenttimetreiksi:
    palacm2 = (pala * pala)
    # neliösenttimetreistä neliömetreiksi:
    palam2 = (palacm2 * 0.0001)
    #tehdään suhde lasku:
    suhde = raha / palam2
    return suhde

print("anna pizzan halkaisia cm:treinä")
halkaisia = float(input())
print("anna pizzan hinta(eur.sent) :")
raha = float(input())

pizza1 = laskuri(halkaisia,raha)

print("anna toisen pizzan halkaisia cm:treinä")
halkaisia = float(input())
print("anna toisen pizzan hinta(eur.sent) :")
raha = float(input())

pizza2 = laskuri(halkaisia,raha)

"""print(f"Ensimmäisen pizzan raha/neliömetri suhde: {pizza1} toisen pizzan suhde {pizza2}")"""
if pizza1 < pizza2:
    print("Ensimmäinen pizza on parempi ostos")
else:
    print("Toinen pizza on parempi ostos")

