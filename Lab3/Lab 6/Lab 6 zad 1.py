def test(imie, wiek=20):
    '''funkcja wypisuje wiek oraz imie
    :param imie:
    :param: wiek:
    :return
    '''
    print(imie, wiek)
test("asd", 14)
test("qwer", 20)
test(wiek=12, imie="gfd")

print(test.__doc__)
print(help(test))
test("kacper")