# Yksi gallona on 3,785 litraa.
print("anna bensan määrä gallonoina, muunnan ne litroiksi: ")

def muunnin (gallon,litre):
    litre = gallon/3.785
    return  litre

while True:
    gallon = float(input())
    if gallon < 0:
        print("ainostaan positiivisia lukuja")
        break
    else:
        litre = muunnin(gallon,None)
        print(f"sinulla on {litre:.2f} l bensaa")
