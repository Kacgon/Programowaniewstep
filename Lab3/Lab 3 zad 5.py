#Grupa laboratoryjna składa się z n studentów (wartość n podaje użytkownik). Wprowadzamy
#liczbę punktów dla każdego studenta. Napisz program, który obliczy średnią liczbę punktów w grupie z
#wykorzystaniem pętli while

n = int(input("podaj liczbe studentow "))
a = 0
i = 1
w = 0
while i <= n:
    x = input("podaj punkty")
    i = i + 1
    w = w + int(x)
else:
    print('wynik to: ' + str(w / n))
