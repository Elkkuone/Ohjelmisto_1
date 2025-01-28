print("anna lukusi, selvitän onko se alkuluku: ")
#haluan että se yrittää jakaa itsensä luvuilla, jos siitä tulee jotain muuta kuin 0 se ei ole alkuluku
no = "tämä luku ei ole alkuluku. "
luku = int(input())
if luku < 1:
    print(no)
else:
   for i in range(luku):
       if i == (luku-2):
           print("tämä luku on alkuluku! ")
           break
       luku2 = luku%(luku-(i+1))
       if int(luku2) == 0:
           print(no)
           break
       else:
           print("trying...")