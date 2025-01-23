i = 0

while i != 5:
    print("käyttäjätunnus")
    ktunnus = input()
    print("salasana")
    salasana = input()
    if ktunnus == "python" and salasana == "rules":
        print("tervetuloa")
    else:
        i +=1
if i == 5:
    print("pääsy evätty")