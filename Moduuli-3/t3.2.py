
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
