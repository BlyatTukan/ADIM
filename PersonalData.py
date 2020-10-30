import random

class CharacterClass:
    def __init__(self, imie, nazwisko, plec, wiek, zawod, zwrost, waga, kolor_wlosow, kolor_oczu, is_play, nickname, online_time):
        #Dane
        self.imie = imie #string
        self.nazwisko = nazwisko #string
        self.plec = plec #string (wybór za pomocą int jeżeli int = 2 to wpisz string)
        self.wiek = wiek #int
        self.zawod = zawod #string
        #Wygląd
        self.zwrost = zwrost #int
        self.waga = waga #float
        self.kolor_wlosow = kolor_wlosow #string
        self.kolor_oczu = kolor_oczu #string
        #Online Data
        self.is_play = is_play #bool
        self.nickname = nickname #string
        self.online_time = online_time #string (wybór za pomocą int)



Character = CharacterClass("","","",0,"",0,0.0,"","",False,"","")

def ChangeGender():
        while 1>0:
            print("Wybierz Płeć\n1. Mężczyzna\n2. Kobieta\n3. Inne")
            Character.plec = input("Wybierz Płeć: ")
            if Character.plec == str(1):
                Character.plec = "Mężczyzna"
                break
            elif Character.plec == str(2):
                Character.plec = "Kobieta"
                break
            elif Character.plec == str(3):
                Character.plec = input("Podaj Swoją Płeć")
                break
            else:
                continue

def ChangeName():
    Character.imie = input("Podaj Imie: ")
    if Character.imie == "":
        if Character.plec == "Mężczyzna":
            Character.imie = random.choice(["Adam","Tomek","Zdziź","Łukasz"])
        elif Character.plec == "Kobieta":
            Character.imie = random.choice(["Ola","Ala","Wiktoria","Alicja"])
        else:
            Character.imie = random.choice(["Jordan","River","Yoshi","Max"])

def ChangeSurname():
    Character.nazwisko = input("Podaj Nazwisko: ")
    if Character.nazwisko == "":
        Character.nazwisko = random.choice(["Kowalski","Smith","Pedro"])

def ChangeAge():
    Character.wiek = input("Podaj Wiek (Rocznikowo): ")
    if Character.wiek == "":
        Character.wiek = random.randrange(0,105)

def ChangeWork():
    Character.zawod = input("Wpisz Zawód: ")
    if Character.zawod == "":
        Character.zawod = random.choice(["Piekarz","Policjant","Strażak","Ratownik"])


def ChangePersonalData():
    #Płeć
    if Character.plec == "":
        ChangeGender()
    else:
        print("Czy Chcesz Zmienić Płeć?")
        TakNie = input("T/N: ")
        while 1>0:
            if TakNie == "T":
                ChangeGender()
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    #FirstName
    if Character.imie == "":
        ChangeName()
    else:
        print("Czy Chcesz Zmienić Imię?")
        TakNie = input("T/N: ")
        while 1>0:
            if TakNie == "T":
                ChangeName()
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    # Nazwisko
    if Character.nazwisko == "":
        ChangeSurname()
    else:
        print("Czy Chcesz Zmienić Nazwisko?")
        TakNie = input("T/N: ")
        while 1>0:
            if TakNie == "T":
                ChangeSurname()
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    # Wiek
    if Character.wiek == 0:
        ChangeAge()
    else:
        print("Czy Chcesz Zmienić Wiek?")
        TakNie = input("T/N: ")
        while 1>0:
            if TakNie == "T":
                ChangeAge()
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    # Zawód
    if int(Character.wiek) > 17:
        if Character.zawod == "":
            ChangeWork()
        else:
            print("Czy Chcesz Zmienić Zawód?")
            TakNie = input("T/N: ")
            while 1>0:
                if TakNie == "T":
                    ChangeWork()
                elif TakNie == "N":
                    break
                else:
                    print("Wybrano nieprawidłową opcję")
                    continue
    else:
        print("Twoja osobowość jest za młody/a by podjąźć")
        Character.zawod = "Bezrobotny"


print("Witaj Użytkowniku")
print("Stwórz swoją drugą osobowość")
print("Zacznijmy od podania danych osobowych")
ChangePersonalData()
print("Twoja Druga Osobowość to:")
print(Character.imie + " " + Character.nazwisko + " (" + Character.plec + ") " + str(Character.wiek) + "lat ")
