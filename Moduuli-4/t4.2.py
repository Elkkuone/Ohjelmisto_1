


print("hei käyttäjä, laita paljonko tuumia ")

i = 1
while i >0:
    i = float(input())
    if i <0:
        print("error")
        break
    cm = i * 2.54
    print(cm)
