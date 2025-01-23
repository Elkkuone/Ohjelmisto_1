import random

print("anna arvauksien määrä: ")
arvausN = int(input())
success = []
for i in range(arvausN):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x ** 2+y ** 2 <1:
        list.append(success,1)
    vaihto = sum(success)
pi = int(vaihto*4)/arvausN
print(str(pi))