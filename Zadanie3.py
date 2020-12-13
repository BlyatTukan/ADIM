import random

class Użytkownik():
    def __init__(self, nazwa, level, ocena, platforma):

        self.nazwa = nazwa
        self.level = level
        if ocena == 0.0:
            self.ocena = random.uniform(1.0,5.0)
        else:
            self.ocena = ocena
        self.ocena = round(self.ocena, 1)
        self.platforma = random.choice(["PC Member", "Mobile Member", "XBOX Member", "PSN Member","Switch Member"])

    def ShowProfile(self):
        print(self.nazwa + "\n" + str(self.level) + " level\n" + str(self.ocena) + "/5\n" + self.platforma + "\n")

    def ChangePlatform(self):
        print("1. PC\n2. Mobile\n3. XBOX\n4. PSN\n5. Switch")
        text = input("Wybierz Platformę konta: ")
        while True:
            if text == "0":
                self.platforma = "PC Member"

class Redaktor(Użytkownik):
    def __init__(self, nazwa, level, ocena, platforma):
        super().__init__(nazwa, level, ocena, platforma)

    def Zmiana(self):
        print("Twoja nazwa konta to: " + self.nazwa)
        text = input("Podaj Nową nazwe konta [kliknij enter by pominąć] ")
        if text != "":
            self.nazwa = text


class Admin(Redaktor):
    def __init__(self, nazwa, level, ocena, platforma):
        super().__init__(nazwa, level, ocena, platforma)

        self.key = 1234

    def printkey(self):
        print(str(self.key))


print ("Tworzenie Obiektów\n")

Konto00 = Admin("Admin", 30, 3.666, 0)
Konto01 = Redaktor("Redaktor", 15, 0.0, 0)
Konto02 = Użytkownik("Użytkownik", 1, 0.0, 0)

print("Printowanie funckji Użytkownika")

Konto02.ShowProfile()

print("Printowanie funckji Redaktora")

Konto01.ShowProfile()
Konto01.Zmiana()

print("Printowanie funckji Admina")

Konto00.ShowProfile()
Konto00.Zmiana()
Konto00.printkey()

print(" ")
Konto00.ChangePlatform()
Konto00.ShowProfile()