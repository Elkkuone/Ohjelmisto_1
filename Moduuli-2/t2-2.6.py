import math
import random


#1


print("mikä on nimesi")
nimi = input()
print("hei " + nimi + " kuinka menee?")


#2


print("mikä on ympyrän säde?")
sade = (int( input()))
pala = (sade**2) * math.pi
print("ympyräsi pinta-ala on " + str(pala))


#3


print("mikä on suorakulmiosi kanta?")
kanta = input()
print("mikä on suorakulmiosi korkeus?")
korkeus = input()
pala = int(kanta) * int(korkeus)
print("suorakulmiosi pinta ala on " + str(pala))


#4


print("anna minulle 3 kokonaislukua:"'\n' "1: ")
yks = int(input())
print("2: ")
kaks = int(input())
print ("3: ")
kolme = int(input())

sum = yks + kaks + kolme
tul = yks * kaks * kolme
kesk = sum / 3
print("lukujesi summa on " + str(sum) +'\n'+ "lukujesi tulo on "+ str(tul) +'\n'+ "lukujesi keskiarvo on " + str(kesk))


#5


print("kerroppas kuinka paljon sinulta löytyy lieviskiä, nauloja ja luoteja"'\n')
print("lieviskät :")
lie = float(input())
print("naulat ")
nau = float(input())
print("luodit ")
luo = float(input())

yht = lie * 20 * 32 * 13.3 + nau *32 *13.3 + luo * 13.3
yhtkg = yht * 0.001

print(str(yhtkg)+ '\n')
print("Sinulla on nykypainolla " +str(int(yhtkg))+ " kilogrammaa ja " + str(int((yhtkg-(int(yhtkg)))*1000)) +  " grammaa")


#6


random.randint(0,9)
random.randint(1,6)

luku1 = (str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
luku2 = (str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6))+str(random.randint(1,6)))



print("tässä on sinun turvalliset salasana viahtohtosi:"+'\n'+ luku1 +'\n'+ luku2)