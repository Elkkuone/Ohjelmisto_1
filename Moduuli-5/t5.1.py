import random

print("kuinka monta d6 noppaa haluat heittää???: ")
lukumäärä = int(input())
noppaluvut = []
for i in range(lukumäärä):
    list.append(noppaluvut, random.randint(1, 6))
print("Noppaheitoista tuli yhteensä " + str(sum(noppaluvut)))
