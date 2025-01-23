print("anna lukusi, selvitän onko se alkuluku: ")
luku = int(input())
x=0
for i in range(luku):
    luku2 = luku % (luku-x)
    print(luku2)
    x= x+1
    if luku2 !=0:
        print("test")
    elif luku2 == 0:
        print("test1")
