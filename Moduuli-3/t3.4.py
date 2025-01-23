
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
