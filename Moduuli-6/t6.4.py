print(" anna lukuja, lasken ne yhteen: laita merkki v kun olet valmis laskemaan luvut yhteen")
luvut = []

def laskuri(luku):
    luku = sum(luvut)
    return luku

while True:
    luku = input()
    if luku == "v":
        print("lukuja on yhteensä: " + str(laskuri(luvut)))
        break
    list.append(luvut,int(luku))
