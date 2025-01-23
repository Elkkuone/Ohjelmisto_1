
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


