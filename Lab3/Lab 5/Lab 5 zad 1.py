import random
x = int(input("podaj ilość liczb"))

lista = []
for i in range(x) :
    wylosowana = random.randint(1, 10)
    lista.append(wylosowana)

print(lista)
x = int(input("podaj liczbe do sprawdzenia"))

if x in lista:
    print("jest w lista")
else:
    print("nie ma w lista")