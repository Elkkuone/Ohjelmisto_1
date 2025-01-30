import math

kuukaudet = "talvi","kevät","kesä","syksy"
print("kerro haluamasi kuukauden numero: ")
luku = int(input())
#jaetaan 3
jako = luku/3
#pyöristetään ylöspäin
pyoristysylos = math.ceil(jako)
print("haluamasi kuuukausi on "+ kuukaudet[pyoristysylos-1])