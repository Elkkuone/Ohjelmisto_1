import random

print("anna arvauksien määrä: ")
arvausN = int(input())
success = []
for i in range(arvausN):
    x = random.randint(-100,100)
    y = random.randint(-100, 100)
    if x^2+y^2 <100:
        list.append(success,1)
    vaihto = sum(success)
pi = int(vaihto*4)/arvausN
print(str(pi))