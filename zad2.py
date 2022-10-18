# Zadanie 2 (2.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała

litera = input("podaj literę")
if(len(litera)>1):
    print("sprawdzono wiecej niz 1 litere")
    exit()
if(len(litera)==0):
    print("nie podano litery")
    exit()
if ("a"<= litera<="z"):
    print("mala litera")
elif("A"<=litera<="Z"):
    print("duza litera")
else:
    print("nie jest litera")