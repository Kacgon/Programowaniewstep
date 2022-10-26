#Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
#liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
#wykorzystaniem pętli while

n = int(input("podaj liczbe studentow "))
a = 0
i = 1
w = 0
while True:
    x = int(input("podaj punkty"))
    if (x<0 or x>100):
        w = w + int(x)
        i = i+1
    if i > n:
        break

print(w/n)
