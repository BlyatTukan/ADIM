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

##### FUNCTION #####

def ChangeGender():
        while 1>0:
            print("Wybierz Płeć\n1. Mężczyzna\n2. Kobieta\n3. Inne")
            Character.plec = input("Wybierz Płeć: ")
            if Character.plec == str(1):
                Character.plec = "Mężczyzna"
                print("Wybrano płeć: \033[32m" + Character.plec + "\033[0m")
                break
            elif Character.plec == str(2):
                Character.plec = "Kobieta"
                print("Wybrano płeć: \033[32m" + Character.plec + "\033[0m")
                break
            elif Character.plec == str(3):
                Character.plec = input("Podaj Swoją Płeć")
                print("Wybrano płeć: \033[32m" + Character.plec + "\033[0m")
                break
            else:
                continue

def ChangeName():
    Character.imie = input("Podaj Imie: ")
    if Character.imie == "":
        if Character.plec == "Mężczyzna":
            Character.imie = random.choice(["Adam","Tomek","Zdziź","Łukasz"])
            print("Wylosowane Imię to \033[32m" + Character.imie + "\033[0m")
        elif Character.plec == "Kobieta":
            Character.imie = random.choice(["Ola","Ala","Wiktoria","Alicja"])
            print("Wylosowane Imię to \033[32m" + Character.imie + "\033[0m")
        else:
            Character.imie = random.choice(["Jordan","River","Yoshi","Max"])
            print("Wylosowane Imię to \033[32m" + Character.imie + "\033[0m")
    else:
        print("Wpisane Imię to \033[32m" + Character.imie + "\033[0m")

def ChangeSurname():
    Character.nazwisko = input("Podaj Nazwisko: ")
    if Character.nazwisko == "":
        Character.nazwisko = random.choice(["Kowalski","Smith","Pedro"])
        print("Wylosowane Nazwisko to \033[32m" + Character.nazwisko + "\033[0m")
    else:
        print("Wpisane Nazwisko to \033[32m" + Character.nazwisko + "\033[0m")

def ChangeAge():
    Character.wiek = input("Podaj Wiek (Rocznikowo): ")
    if Character.wiek == "":
        Character.wiek = random.randrange(0,105)
        print("Wylosowany Wiek to \033[32m" + str(Character.wiek) + "\033[0m")
    else:
        print("Wpisany Wiek to \033[32m" + str(Character.wiek) + "\033[0m")

def ChangeWork():
    Character.zawod = input("Wpisz Zawód: ")
    if Character.zawod == "":
        Character.zawod = random.choice(["Piekarz","Policjant","Strażak","Ratownik"])
        print("Wylosowany Zawód to \033[32m" + Character.zawod + "\033[0m")
    else:
        print("Wpisany Zawód to \033[32m" + Character.zawod + "\033[0m")


def ChangePersonalData():
    #Płeć
    if Character.plec == "":
        ChangeGender()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Płeć?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeGender()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    #FirstName
    if Character.imie == "":
        ChangeName()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Imię?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeName()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Nazwisko
    if Character.nazwisko == "":
        ChangeSurname()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Nazwisko?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeSurname()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Wiek
    if Character.wiek == 0:
        ChangeAge()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Wiek?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeAge()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Zawód
    if int(Character.wiek) > 17:
        if Character.zawod == "":
            ChangeWork()
        else:
            while 1>0:
                print("Czy Chcesz Zmienić Zawód?")
                TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
                if TakNie == "T":
                    ChangeWork()
                    break
                elif TakNie == "N":
                    break
                else:
                    print("\033[31mWybrano nieprawidłową opcję\033[0m")
                    continue
    else:
        print("Musisz Ukończyć \033[31m18 \033[0mlat, by móc zacząć pracować")
        Character.zawod = "Bezrobotny"

##### PRIVATE #####

isSetPersonalData = False

##### CODE #####

print("Witaj Użytkowniku")
print("Stwórz swoją drugą osobowość")
print("Zacznijmy od podania danych osobowych")
while isSetPersonalData == False:
    ChangePersonalData()
    print("Czy Wpisane przez Ciebie dane są prawidłowe?")
    print("Imię: \033[35m" + Character.imie + "\033[0m" + ", Nazwisko: \033[35m" + Character.nazwisko + "\033[0m" + ", Płeć: \033[35m" + Character.plec + "\033[0m" + ", Wiek: \033[35m" + str(Character.wiek) + "lat\033[0m" + ", Zawód: \033[35m" + Character.zawod + "\033[0m")
    while 1 > 0:
            git_dane = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if git_dane == "T":
                isSetPersonalData = True
                break
            elif git_dane == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    continue

print("Twoja Druga Osobowość to:")
print(Character.imie + " " + Character.nazwisko + " (" + Character.plec + ") " + str(Character.wiek) + "lat ")
