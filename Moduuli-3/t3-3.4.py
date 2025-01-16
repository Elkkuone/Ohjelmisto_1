


#1


print("kuinka pitkä kuhasi on senttimetreissä?")
pit = float(input())
if pit >= 37:
    print("tämä on tarpeeksi suuri kala")
else:
    print("tämä kala on liian pieni")


#2


print("hei laivan käyttäjä, kirjoita hyttiluokkasi saadaksesti hyttisi kuvauksen: ")
sana = str(input())
if sana == "LUX":
    print("parvekkeellinen hytti yläkannella")
elif sana == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella")
elif sana == "B":
    print("B on ikkunaton hytti autokannen yläpuolella")
elif sana == "C":
    print("C on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")



#3


print("hei käyttäjä, oletko mies vai nainen? ")
mvn = input()
if mvn == "mies" or "Mies":
    print("Seuraavaksi anna sinun  hemoglobiiniarvosi yksikössä(g/l): ")
    hemog = float(input())
    if hemog < 134:
        print("hemoglobiiniarvosi on alhainen")
    elif 134 < hemog < 195:
        print("hemoglobiiniarvosi on normaali")
    elif hemog >195:
        print("hemoglobiiniarvosi on korkea")
elif mvn == "Nainen" or "nainen":
    print("Seuraavaksi anna sinun  hemoglobiiniarvosi yksikössä(g/l):")
    hemog = float(input())
    if hemog < 117:
        print("hemoglobiiniarvosi on alhainen")
    elif 117 < hemog < 175:
        print("hemoglobiiniarvosi on normaali")
    elif hemog > 175:
        print("hemoglobiiniarvosi on korkea")



#4


print("hei, kerro minulle vuosi ja lasken onko se karkausvuosi: ")
vuosi = int(input())
testi= 0

if vuosi % 4 == testi:#onko jaollinen 4
    if vuosi %100 ==testi:#onko myös jaollinen 100, jos ei ole niin ei tarvitse katsoa jatkotarksitusta
        if vuosi %400 == testi:# jos on jaollinen 100 ja 400, on karkausvuosi,muuten ei ole
            print("tämä vuosi on karkausvuosi")
        else:
            print("tämä vuosi ei ole karkausvuosi")
    else:
        print("tämä vuosi on karkausvuosi")
else:
    print("tämä vuosi ei ole karkausvuosi")
