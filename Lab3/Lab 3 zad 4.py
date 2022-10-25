
x = int(input('podaj 1'))
z = int(input('podaj 2'))

if x > z:
    x,z = z,x

while z>=x:
    if x%2 == 1:
        x = x + 1
        continue
    print(x, end=' ')
    x = x + 1

