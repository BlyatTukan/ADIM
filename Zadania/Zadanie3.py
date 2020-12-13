import random

class Użytkownik():
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

class Redaktor(Użytkownik):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)


    def Zmiana(self):
        print("    Twoja nazwa konta to: " + self.nazwa)
        text = input("    Podaj Nową nazwe konta [kliknij enter by pominąć] ")
        if text != "":
            self.nazwa = text
            print("    Zmieniono Nazwę Konta na " + text)

        print("    Twój level konta to: " + str(self.level))
        text = int(input("    Podaj Nowy level konta [kliknij enter by pominąć] ") or 0)
        if text == 0:
            pass
        else:
            self.level = text
            print("    Zmieniono Level Konta na " + str(text))

        print("    Twoja ocena konta to: " + str(self.ocena))
        text = float(input("    Podaj Nową ocene konta [kliknij enter by pominąć] ") or 0.0)
        if text == 0.0:
            pass
        else:
            self.ocena = text
            print("    Zmieniono Nazwę Konta na " + str(text))



class Admin(Redaktor):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

        self.key = str(random.randrange(100000000000000,9999999999999999)

    def printkey(self):
        print(str(self.key))


#### Tworzenie Obiektów Klasy ####
Admin = Admin("Administrator", 30, "")
Redaktor = Redaktor("Redaktor", 30, "")
Użytkownik = Użytkownik("Użytkownik", 30, "")

print("\nMożliwości Użytkownika:")

print("Możliwości Redaktora:")
print("    - Modyfikacja pól")
print("- Modyfikacja pól Redaktora")
Redaktor.Zmiana()

print("Możliwości Administratora:")
print("    - Modyfikacja pól\n    - Printowanie Kodu Admina")
print("- Modyfikacja pól Administratora [wraz z platformą]")
Admin.Zmiana()
print("- Printowanie Kodu Administratora")
Admin.printkey()