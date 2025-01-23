












# en saanut toimimaan, tein uudestaan








import random


print("kerro arvottavien pisteiden määrä :")
arvausN = int(input())
#n = sisälle jäävien pisteiden määrä
# pi = 4*n/N
# jääkö yksikköympyrä = 0.0
n = 0
i = 0
while i < arvausN +1:
    x = random.randint(1,-1)
    y = random.randint(1,-1)
    print(str(x)+str(y))
    if x^2+y^2 <1 == True:
        i +=1
        print("test")

    elif i == arvausN:
        print("test66")
        print
        break
    else:
        i += 1
# x^2+y^2<1
print("test4 " +str(n))
pi = (n*4)/arvausN
vastaus = int(pi)



print("piin likiarvo on :" + str(vastaus))