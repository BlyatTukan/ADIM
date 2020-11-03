##### IMPORT #####

import random

##### CLASS #####

class CharacterClass:
    def __init__(self, imie, nazwisko, plec, wiek, zawod, zwrost, waga, kolor_wlosow, kolor_oczu, is_play, nickname, online_time, person_id):
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
        self.online_time = online_time #int 
        self.person_id = person_id #string (zawsze losowy) 

Character = CharacterClass("","","",0,"",0,0.0,"","",False,"",0,"")

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
    Character.wiek = int(input("Podaj Wiek (Rocznikowo): ") or "0")
    if Character.wiek == 0:
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

def ChangeHeight():
    Character.zwrost = int(input("Podaj Zwrost (w centrymetrach): ") or "0")
    if Character.zwrost == 0:
        Character.zwrost = random.randrange(130,220)
        print("Wylosowany Zwrost to \033[32m" + str(Character.zwrost) + "\033[0m")
    else:
        print("Wpisany Zwrost to \033[32m" + str(Character.zwrost) + "\033[0m")

def ChangeWeight():
    Character.waga = float(input("Podaj swoją wagę (w centrymetrach): ") or "0")
    if Character.waga == 0:
        Character.waga = random.uniform(40.0,150.0)
        Character.waga = round(Character.waga, 1)
        print("Wylosowana Waga to \033[32m" + str(Character.waga) + "\033[0m KG")
    else:
        print("Wpisana Waga to \033[32m" + str(Character.waga) + "\033[0m KG")

def ChangeEye():
    Character.kolor_oczu = input("Podaj Kolor Oczu: ")
    if Character.kolor_oczu == "":
        Character.kolor_oczu = random.choice(["Zielone","Niebieski","Piwne"])
        print("Wylosowany Kolor Oczu to \033[32m" + Character.kolor_oczu + "\033[0m")
    else:
        print("Wpisany Kolor Oczu to \033[32m" + Character.kolor_oczu + "\033[0m")

def ChangeHair():
    Character.kolor_wlosow = input("Podaj Kolor Włosów: ")
    if Character.kolor_wlosow == "":
        Character.kolor_wlosow = random.choice(["Blond","Rude","Brązowe", "Czarne"])
        print("Wylosowanny Kolor Włosów to \033[32m" + Character.kolor_wlosow + "\033[0m")
    else:
        print("Wpisanny Kolor Włosów to \033[32m" + Character.kolor_wlosow + "\033[0m")

def ChangeNickname():
    Character.nickname = input("Podaj swój nick: ")
    if Character.nickname == "":
        Character.nickname = random.choice(["Zielone","Niebieski","Piwne"])
        print("Wylosowany Nick to \033[32m" + Character.nickname + "\033[0m")
    else:
        print("Wpisany Nick to \033[32m" + Character.nickname + "\033[0m")

def ChangeOnlineTime():
    Character.online_time = int(input("Podaj Czas Spędzany Online: ") or "0")
    if Character.online_time == 0:
        Character.online_time = random.uniform(0.0,8.0)
        Character.online_time = round(Character.online_time, 1)
        print("Wylosowany Czas Spędzany Online to \033[32m" + str(Character.online_time) + "\033[0mh")
    else:
        print("Wpisany Czas Spędzany Online to \033[32m" + str(Character.online_time) + "\033[0mh")

def ChangePersonalData():
    # Płeć
    if Character.plec == "":
        ChangeGender()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Płeć? ")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeGender()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Imię
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

def ChangeCharacterLook():
    # Zwrost
    if Character.zwrost == 0:
        ChangeHeight()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Zwrost?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeHeight()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Waga
    if Character.waga == 0:
        ChangeWeight()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Wagę?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeWeight()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Kolor Oczu
    if Character.kolor_oczu == "":
        ChangeEye()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Kolor Oczu?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeEye()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    # Kolor Włosów
    if Character.kolor_wlosow == "":
        ChangeHair()
    else:
        while 1>0:
            print("Czy Chcesz Zmienić Kolor Włosów?")
            TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if TakNie == "T":
                ChangeHair()
                break
            elif TakNie == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue

def ChangeOnlineData():
    print("Czy Chcesz Wpisać Dane Online? ")
    while True:
        TrueFalse = input("\033[32mT\033[0m/\033[31mF\033[0m: ")
        if TrueFalse == "T":
            Character.is_play = True
            print("Wybrano że postać \033[32mużywa\033[0m internetu")
            break
        elif TrueFalse == "F":
            Character.is_play = False
            print("Wybrano że postać \033[31mnie używa\033[0m internetu")
            break
        else:
            print("\033[31mWybrano nieprawidłową opcję\033[0m")
            continue
    if Character.is_play == True:
        # Nickname
        if Character.nickname == "":
            ChangeNickname()
        else:
            while True:
                print("Czy Chcesz Zmienić Nick?")
                TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
                if TakNie == "T":
                    ChangeNickname()
                    break
                elif TakNie == "N":
                    break
                else:
                    print("\033[31mWybrano nieprawidłową opcję\033[0m")
                    continue
        # Średni Czas Gry
        if Character.online_time == 0:
            ChangeOnlineTime()
        else:
            while True:
                print("Czy Chcesz Zmienić Czas Spędzany Online?")
                TakNie = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
                if TakNie == "T":
                    ChangeOnlineTime()
                    break
                elif TakNie == "N":
                    break
                else:
                    print("\033[31mWybrano nieprawidłową opcję\033[0m")
                    continue
    
##### PRIVATE #####

isSetPersonalData = False
isSetLook = False
isSetOnlineData = False

##### CODE #####

print("Witaj Użytkowniku")
print("Stwórz swoją wirtualną kopię")
print("Zacznijmy od podania danych osobowych")
while isSetPersonalData == False: 
    ChangePersonalData() 
    print("Czy Wpisane przez Ciebie dane są prawidłowe?")
    print("Imię: \033[35m" + Character.imie + "\033[0m" + ", Nazwisko: \033[35m" + Character.nazwisko + "\033[0m" + ", Płeć: \033[35m" + Character.plec + "\033[0m" + ", Wiek: \033[35m" + str(Character.wiek) + "lat\033[0m" + ", Zawód: \033[35m" + Character.zawod + "\033[0m")
    while True:
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
print("Widzę że, wpisałeś już dane osobiste")
print("Teraz wpisz wygląd postaci")
while isSetLook == False:
    ChangeCharacterLook() #pętle
    print("Czy Wybrany przez Ciebie wygląd są prawidłowy?")
    print("Zwrost: \033[35m" + str(Character.zwrost) + "cm\033[0m" + ", Waga: \033[35m" + str(Character.waga) + "kg\033[0m" + ", Kolor Oczu: \033[35m" + Character.kolor_oczu + "\033[0m" + ", Kolor Włosów: \033[35m" + Character.kolor_wlosow)
    while True:
            git_dane = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if git_dane == "T":
                isSetLook = True
                break
            elif git_dane == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    continue
print("To Teraz Przechodzimy do dodatkowych danych")
while isSetOnlineData == False:
    ChangeOnlineData() #pętle
    print("Czy Wybrane przez Ciebie dodatkowe dane są prawidłowy?")
    print("Korzystanie z internetu: \033[35m" + str(Character.is_play) + "\033[0m" + ", Nickname: \033[35m" + Character.nickname + "\033[0m" + ", Czas Spędzany Online: \033[35m" + str(Character.online_time) + "h\033[0m")
    while True:
            git_dane = input("\033[32mT\033[0m/\033[31mN\033[0m: ")
            if git_dane == "T":
                isSetOnlineData = True
                break
            elif git_dane == "N":
                break
            else:
                print("\033[31mWybrano nieprawidłową opcję\033[0m")
                continue
    continue

print("Twoja Druga Osobowość to:\n")
if Character.is_play == False:
    print(Character.imie + " " + Character.nazwisko + " (" + Character.plec + ") " + str(Character.wiek) + "lat ")
else:
    print(Character.imie + ' "' + Character.nickname + '" ' + Character.nazwisko + " (" + Character.plec + ") " + str(Character.wiek) + "lat ")

print("Zwrost: "+str(Character.zwrost/100)+"m" + ", Waga: "+str(Character.waga)+"kg" + ", Kolor Oczu: "+str(Character.kolor_oczu)+"" + ", Kolor Włosów: "+str(Character.kolor_wlosow))

Character.person_id = str(random.randrange(1000,9999)) + "-" + str(random.randrange(1000,9999)) + "-" + str(random.randrange(1000,9999)) + "-" + str(random.randrange(1000,9999))

if Character.is_play == True:
    print("Czas Spędzany Online: " + str(Character.online_time) + ", Person ID: " + Character.person_id)
else:
    print("Person ID: " + Character.person_id)

print("Sprawy Zdrowotne")

# BMI i czas przy kompie

BMI = Character.waga / ((Character.zwrost/100)**2)
print("Twoje BMI Wynosi: " + str(round(BMI, 2)))
if(BMI < 16):
    print("Jesteś Wygłodzony")
elif(BMI < 17):
    print("Jesteś Wychudzony")
elif(BMI < 18.5):
    print("Masz Niedowagę")
elif(BMI < 25):
    print("Masz idealną wagę")
elif(BMI < 30):
    print("Masz Nadwagę")
elif(BMI < 35):
    print("Masz Otyłość I Stopnia")
elif(BMI < 40):
    print("Masz Otyłość II Stopnia")
else:
    print("Masz Skrajną Otyłość")

if Character.wiek < 2:
    if(Character.online_time > 0):
        print("Nie spędzasz za dużó czasu przed ekranami")
    else:
        print("Spędzasz o " + str((Character.online_time - 0)) + "h za dużo przed ekranami")
elif Character.wiek < 6:
    if(Character.online_time > 0.25):
        print("Nie spędzasz za dużó czasu przed ekranami")
    else:
        print("Spędzasz o " + str((Character.online_time - 0.25)) + "h za dużo przed ekranami")
elif Character.wiek < 12:
    if(Character.online_time > 1.5):
        print("Nie spędzasz za dużó czasu przed ekranami")
    else:
        print("Spędzasz o " + str((Character.online_time - 1.5)) + "h za dużo przed ekranami")
else:
    if(Character.online_time > 2.5):
        print("Nie spędzasz za dużó czasu przed ekranami")
    else:
        print("Spędzasz o " + str((Character.online_time - 2.5)) + "h za dużo przed ekranami")
            