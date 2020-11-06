##### IMPORT #####

import PrzelicznikJednostek #
import CharacterScript # Ukończone
import RzutKoscia # Ukończone
import DzialanaNaLiczbach #

##### FUNCTION #####

def WybieranieOpcji():
    print("1. Przeliczanie Jednostek\n2. Rzut Kością\n3. Działania Na Liczbach\n4. Dane Osobowe")
    wybrana_opcja = input("Wybierz który program chcesz uruchomić: ")
    while True:
        if wybrana_opcja == "1": #Przelicznik
            PrzelicznikJednostek.CelsjuszNaFahrenheit(100)
            PrzelicznikJednostek.FahrenheitNaCelsjusz(100)
            PrzelicznikJednostek.FuntyNaKilogramy(100)
            PrzelicznikJednostek.KilogramyNaFunty(100)
            break
        elif wybrana_opcja == "2": #Rzut Zrobione
            liczba = int(input("Podaj Liczbę rzutów kostką: ") or "1")
            RzutKoscia.Rzut(liczba)
            break
        elif wybrana_opcja == "3": #Działania
            print("     1. Pitagoras (bok a, bok b)\n     2. Pitagoras (bok a, przekątka)\n     3. Pitagoras (bok b, przekątka)\n     4. Objętość Kuli\n     5. Pole Kuli\n     6. Przekrój Kuli\n     7. Objętość Prostopadłościanu\n     8. Pole Prostopadłościanu")
            wybrane_dzialanie = input("     Wybierz działanie: ")
            if wybrane_dzialanie == "1":
                a = input("     Bok A: ")
                b = input("     Bok B: ")
                print("     Pitagoras Wynosi: \033[32m" + str(DzialanaNaLiczbach.pitagoras_c(a, b)) + "\033[0m")
            if wybrane_dzialanie == "2":
                a = input("     Bok A: ")
                c = input("     Bok C: ")
                print("     Pitagoras Wynosi: \033[32m" + str(DzialanaNaLiczbach.pitagoras_b(a, c)) + "\033[0m")
            if wybrane_dzialanie == "3":
                b = input("     Bok B: ")
                c = input("     Bok C: ")
                print("     Pitagoras Wynosi: \033[32m" + str(DzialanaNaLiczbach.pitagoras_a(b, c)) + "\033[0m")
            if wybrane_dzialanie == "4":
                r = input("     Promień Koła: ")
                print("     Objętość Kuli: \033[32m" + str(DzialanaNaLiczbach.ObjetoscKuli(r))+ "\033[0m")
            if wybrane_dzialanie == "5":
                r = input("     Promień Koła: ")
                print("     Pole Kuli: \033[32m" + str(DzialanaNaLiczbach.PolePowieszchniKuli(r))+ "\033[0m")
            if wybrane_dzialanie == "6":
                r = input("     Promień Koła: ")
                print("     Przekrój Kuli: \033[32m" + str(DzialanaNaLiczbach.PrzekrojKuli(r))+ "\033[0m")
            if wybrane_dzialanie == "7":
                a = input("     Bok A: ")
                b = input("     Bok B: ")
                c = input("     Bok C: ")
                print("     Objętość Prostopadłościanu: \033[32m" + str(DzialanaNaLiczbach.ObjętośćProstopadloscian(a,b,c))+ "\033[0m")
            if wybrane_dzialanie == "8":
                a = input("     Bok A: ")
                b = input("     Bok B: ")
                c = input("     Bok C: ")
                print("     Objętość Prostopadłościanu: \033[32m" + str(DzialanaNaLiczbach.PoleProstopadloscian(a,b,c))+ "\033[0m")
            break
        elif wybrana_opcja == "4": #Dane Osobowe
            CharacterScript.GeneratePerson()
            CharacterScript.Health()
            break
        elif wybrana_opcja == "": #Wyjdź ze scryptu
            print("Smutne że tak szybko nas opuszczasz\n0 Impostors remain")
            break
        else: #Zła Opcja
            print("Zła Odp")
            continue

##### PRIVATE #####

_private = True

##### CODE #####

print("Witaj Użytkowniku")
WybieranieOpcji()
