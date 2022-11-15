z = int(input("podaj liczbe zwierzat"))

zwierzeta = []
for i in range(z):
    x = input("podaj zwierze")
    zwierzeta.append(x)
print(zwierzeta[0], zwierzeta[-3], zwierzeta[-2], zwierzeta[-1])

print(sorted(zwierzeta))