x = int(input('podaj 1'))
z = int(input('podaj 2'))

if x > z:
    x,z = z,x

while z>=x:
    print(x, end=' ')
    x=x+1 