
print("anna lukuja, sitten kun laitat välilyönnin, ohjelma antaa 5 suurinta")
luvut = []
while True:
    luku = input()
    if str(luku) == "" or str(luku) == " ":
        luvut.sort(reverse=True)
        print("5 suurinta on: " + str(luvut[:5]))
        break
    list.append(luvut,int(luku))