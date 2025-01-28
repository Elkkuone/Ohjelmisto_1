





# tein tehtävän lukematta ohjeita loppuun asti, toimii muttei toimi kuvatulla tavalla






import random
heitot = []
print("hei käyttäjä, anna yläraja nopna luvulle: ")
yläraja = int(input())
def noppa(heitto,yläraja):
    heitto= random.randint(1, yläraja)
    return heitto


while True:
    heitto = noppa(None,yläraja)
    if heitto == yläraja:
        print(f"Nopasta tuli {heitto} onneksi olkoon!")
        list.append(heitot,heitto)
        print("Yhteensä silmäluvista tulee " + str(sum(heitot)))
        break
    else:
        print(f"Nopasta tuli {heitto} ")
        list.append(heitot,heitto)
