
liczby=[]
for i in range(5) :
    x = int(input("podaj liczbe"))
if x%3 == 1 :
    liczby.append(x)
else:
    print("nie podzielna")
print(liczby)