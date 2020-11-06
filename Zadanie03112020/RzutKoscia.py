import random

def Rzut(ilosc):
    _index = 0
    _ilosc_punktow = 0
    while int(ilosc) > _index:
        _wygenerowana_liczba = random.randint(1,6)
        if _wygenerowana_liczba == 1:
            print("-----------\n|         |\n|    o    |\n|         |\n-----------")
        if _wygenerowana_liczba == 2:
            print("-----------\n|  o      |\n|         |\n|      o  |\n-----------")
        if _wygenerowana_liczba == 3:
            print("-----------\n|  o      |\n|    o    |\n|      o  |\n-----------")
        if _wygenerowana_liczba == 4:
            print("-----------\n|  o   o  |\n|         |\n|  o   o  |\n-----------")
        if _wygenerowana_liczba == 5:
            print("-----------\n|  o   o  |\n|    o    |\n|  o   o  |\n-----------")
        if _wygenerowana_liczba == 6:
            print("-----------\n|  o   o  |\n|  o   o  |\n|  o   o  |\n-----------")
        _ilosc_punktow += _wygenerowana_liczba
        _index += 1
        continue
    print("Liczba uzyskanych punktów: "  + str(_ilosc_punktow))