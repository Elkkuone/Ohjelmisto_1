import random


def noppa(heitto):

    heitto= random.randint(1, 6)
    return heitto


while True:
    heitto = noppa(None)
    if heitto == 6:
        print(f"Nopasta tuli {heitto} onneksi olkoon!")
        break
    else:
        print(f"Nopasta tuli {heitto} voi harmi!")
