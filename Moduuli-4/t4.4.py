import random

i = True
print("hei, yritä arvata minkä luvun keksin 1 ja 10 väliltä")
oikea = random.randint(1,10)
while i:
    arvaus = float(input())
    if arvaus > oikea:
        print("liian iso")
    elif arvaus < oikea:
        print("liian pieni")
    else:
        print("oikein!")
        break