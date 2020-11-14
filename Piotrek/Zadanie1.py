import random #do losowych wartości w kodzie

class NazwaClasy:
    def __init__(self, wartosc_int, wartosc_float, wartosc_string):
        self.wartosc_int = wartosc_int
        self.wartosc_float = wartosc_float
        self.wartosc_string = wartosc_string

    def Zmiana_wartość_int(self): #to self musi być i tyle          ### FUNKCJA W KLASIE ###
        self.wartosc_int = int(input("Podaj wartosc_int: ") or 0)
        if self.wartosc_int == 0:
            self.wartosc_int = random.randrange(0,100) # Liczba od 0 do 100 np. 3, 69, 32
            print("Wylosowane wartosc_int to " + str(self.wartosc_int))
        else:
            print("Wpisane wartosc_int to " + str(self.wartosc_int))

    def Zmiana_wartość_float(self): #to self musi być i tyle          ### FUNKCJA W KLASIE ###
        self.wartosc_float = float(input("Podaj wartosc_float: ") or 0)
        if self.wartosc_float == 0:
            self.wartosc_float = random.uniform(0.0,100.0) # Liczba od 0 do 100 np. 4.2, 93.2, 89.4
            print("Wylosowane wartosc_float to " + str(self.wartosc_float))
        else:
            print("Wpisane wartosc_int to " + str(self.wartosc_float))

    def Zmiana_wartość_string(self): #to self musi być i tyle          ### FUNKCJA W KLASIE ###
        self.wartosc_string = input("Podaj wartosc_string: " or "")
        if self.wartosc_string == "":
            self.wartosc_string = random.choice(["STRING","TEKST","LOREM IPSUM"]) # STRING, TEKST albo LOREM IPSUM
            print("Wylosowane wartosc_string to " + str(self.wartosc_string))
        else:
            print("Wpisane wartosc_string to " + str(self.wartosc_string))


def FunkcjaZmianyWartosci():          ### FUNKCJA W SCRYPCIE ###
    while True:
        ObiektUżywającyClasy.Zmiana_wartość_int()
        ObiektUżywającyClasy.Zmiana_wartość_float()
        ObiektUżywającyClasy.Zmiana_wartość_string()
        while True:
            print("Czy Chcesz Zmienić Czas Spędzany Online?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                FunkcjaZmianyWartosci()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
        break


ObiektUżywającyClasy = NazwaClasy(4, 2.1, "string") #wartosc_int = 4, wartosc_float = 2.1, wartosc_string = "string"
print("WPROWADZENIE")
FunkcjaZmianyWartosci()
print("WYPISANIE WARTOŚCI")
print("int: " + str(ObiektUżywającyClasy.wartosc_int) + "float: " + str(ObiektUżywającyClasy.wartosc_float) + "string: " + str(ObiektUżywającyClasy.wartosc_string))
print("ZAKOŃCZENIE")

    