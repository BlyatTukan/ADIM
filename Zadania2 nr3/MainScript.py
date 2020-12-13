import time
import random
import types

    #### KLASA SYSTEM ####  

class System:
    def __init__ (self, Procesor, KartaGraficzna, PamięcRam, Dysk):
        if(Procesor == ""):
            self.Procek = random.choice(["\033[35mApple M1\033[0m","\033[36mIntel I3 Series\033[0m","\033[36mIntel I5 Series\033[0m","\033[36mIntel I7 Series\033[0m","\033[36mIntel I9 Series\033[0m", "\033[31mAMD 3 Series\033[0m", "\033[31mAMD 5 Series\033[0m", "\033[31mAMD 7 Series\033[0m"])
        else:
            self.Procek = Procesor   #String

        if(KartaGraficzna == ""):
            self.Grafika = random.choice(["\033[32mNvidia GTX Series\033[0m", "\033[32mNvidia RTX Series\033[0m", "\033[31mAMD Radeon Series\033[0m", "\033[36mIntel XE\033[0m"])
        else:
            self.Grafika = KartaGraficzna   #String

        if(PamięcRam == 0):
            self.Ram = random.choice([4, 8, 16, 32, 64, 128])
        else:
            self.Ram = PamięcRam   #Int

        if(Dysk == 0):
            self.Dysk = random.choice([128, 256, 512, 1024, 2048, 4096])
        else:
            self.Dysk = Dysk   #Int

        self.ToSystem = True
        self.Dostęp_Admin = False
        self.Dostęp_Redaktor = False

        self.AdminList = []   #LISTA
        self.RedaktorList = []   #LISTA
        self.UsersList = []   #LISTA

        self.ZalogowanyTypKonta = 3 #   3-Admin,  2-Redaktor,   1-User
        self.ZalogowanyAdmin = 0
        self.ZalogowanyRedaktor = 0
        self.ZalogowanyUżytkownik = 0

    #### FUNKCJE W KLASIE "SYSTEM" ####

    def ZmienPodzespoły(self):
        self.Procek = random.choice(["\033[35mApple M1\033[0m","\033[36mIntel I3 Series\033[0m","\033[36mIntel I5 Series\033[0m","\033[36mIntel I7 Series\033[0m","\033[36mIntel I9 Series\033[0m", "\033[31mAMD 3 Series\033[0m", "\033[31mAMD 5 Series\033[0m", "\033[31mAMD 7 Series\033[0m"])
        self.Grafika = random.choice(["\033[32mNvidia GTX Series\033[0m", "\033[32mNvidia RTX Series\033[0m", "\033[31mAMD Radeon Series\033[0m", "\033[36mIntel XE\033[0m"])
        self.Ram = random.choice([4, 8, 16, 32, 64, 128])
        self.Dysk = random.choice([128, 256, 512, 1024, 2048, 4096])
    
    def WyświetlPodzespoły(self):
        if self.ToSystem == True:
            print("Podzespoły komputera")
        elif self.Dostęp_Admin == True:
            print("Podzespoły komputera zdalnego administratora")
        elif self.Dostęp_Redaktor == True:
            print("Podzespoły komputera zdalnego redaktora")
        else:
            print("Podzespoły komputera zdalnego użytkownika")
        print("Procesor: " + self.Procek + "\nKarta Graficzna: "  + self.Grafika + "\nPamięć Ram: \033[33m"  + str(self.Ram) + "GB\033[0m\nDysk Twardy: \033[33m"  + str(self.Dysk) + "GB\033[0m\n")

    def UruchamianieSystemu(self):
        time.sleep(random.uniform(0.3, 1))
        print("Uruchamianie " + str(random.randrange(1,29)) + " %")
        time.sleep(random.uniform(0.3, 1))
        print("Uruchamianie " + str(random.randrange(30,55)) + " %")
        time.sleep(random.uniform(0.3, 1))
        print("Uruchamianie " + str(random.randrange(56,68)) + " %")
        time.sleep(random.uniform(0.3, 1))
        print("Uruchamianie " + str(random.randrange(69,80)) + " %")
        time.sleep(random.uniform(0.3, 1))
        print("Uruchamianie " + str(random.randrange(81,99)) + " %")
        time.sleep(random.uniform(0.3, 1))
        print("\nWitaj w Glass OS")

    def SprawdźUprawnienia(self):
        if self.Dostęp_Admin == True:
            print("Admin" + self.Name)
        elif self.Dostęp_Redaktor == True:
            print("Redaktor")
        else:
            print("Użytkownik")

    def WypiszIlośćUżytkowników(self):
        _admini = 0
        print("Ilość Adminów: " + str(len(self.AdminList)))
        while _admini < len(self.AdminList):
            print ("    " + str(self.AdminList[_admini].Name))
            _admini += 1
        _Redaktor = 0
        print("Ilość Redaktorów: " + str(len(self.RedaktorList)))
        while _Redaktor < len(self.RedaktorList):
            print ("    " + str(self.RedaktorList[_Redaktor].Name))
            _Redaktor += 1
        _Users = 0
        print("Ilość Użytkowników: " + str(len(self.UsersList)))
        while _Users < len(self.UsersList):
            print ("    " + str(self.UsersList[_Users].Name))
            _Users += 1

    def DodawanieNowychKont(self):
        print("    Utwórz nowe konto\n    1. Użytkownika\n    2. Redaktora\n    3. Admina\n    wybierz dowolny inny klawisz by anulować")
        while True:
            TypKonta = input("    Wpisz cyfrę zabezpieczeń nowego konta: ") or "0"
            if TypKonta == "1":
                self.UsersList.append(Użytkownik("","",0,0,""))
                self.UsersList[len(self.UsersList) - 1].Name = input("    Wpisz nazwę nowego konta: ")
                print("    Dodano Nowe Konto Użytkownika o nazwie: " + self.UsersList[len(self.UsersList) - 1].Name)
                continue
            if TypKonta == "2":
                self.RedaktorList.append(Redaktor("","",0,0,""))
                self.RedaktorList[len(self.RedaktorList) - 1].Name = input("    Wpisz nazwę nowego konta: ")
                print("    Dodano Nowe Konto Redaktora o nazwie: " + self.RedaktorList[len(self.RedaktorList) - 1].Name)
                continue
            if TypKonta == "3":
                self.AdminList.append(Admin("","",0,0,""))
                self.AdminList[len(self.AdminList) - 1].Name = input("    Wpisz nazwę nowego konta: ")
                print("    Dodano Nowe Konto Administratora o nazwie: " + self.AdminList[len(self.AdminList) - 1].Name)
                continue
            else:
                break

    def Wybórkonta(self):
        print("1. Użytkownik    2. Redaktor    3. Admin")
        WybierzTypKonta = input("Wybierz typ konta: ")
        if WybierzTypKonta == "3":
            if len(self.AdminList) > 0:
                _admini = 0
                self.ZalogowanyTypKonta = WybierzTypKonta
                while _admini < len(self.AdminList):
                    print (str(_admini) + ". " + str(self.AdminList[_admini].Name))
                    _admini += 1
                while True:
                    wybranekonto = int(input("Wybierz konto: "))
                    if wybranekonto < len(self.AdminList):
                        print("Zalogowano się na konto administratora " + self.AdminList[wybranekonto].Name)
                        self.ZalogowanyAdmin = wybranekonto
                        break
                    else:
                        print("Nieprawidłowe informacje")
                        continue
            else:
                print("Nie ma żadnych kont administratora w tym systemie")
        if WybierzTypKonta == "2":
            if len(self.RedaktorList) > 0:
                _redaktor = 0
                self.ZalogowanyTypKonta = WybierzTypKonta
                while _redaktor < len(self.RedaktorList):
                    print (str(_redaktor) + ". " + str(self.RedaktorList[_redaktor].Name))
                    _redaktor += 1
                while True:
                    wybranekonto = int(input("Wybierz konto: "))
                    if wybranekonto < len(self.RedaktorList):
                        print("Zalogowano się na konto redaktora " + self.RedaktorList[wybranekonto].Name)
                        self.ZalogowanyRedaktor = wybranekonto
                        break
                    else:
                        print("Nieprawidłowe informacje")
                        continue
            else:
                print("Nie ma żadnych kont redaktora w tym systemie")
        if WybierzTypKonta == "1":
            if len(self.UsersList) > 0:
                _Users = 0
                self.ZalogowanyTypKonta = WybierzTypKonta
                while _Users < len(self.UsersList):
                    print (str(_Users) + ". " + str(self.UsersList[_Users].Name))
                    _Users += 1
                while True:
                    wybranekonto = int(input("Wybierz konto: "))
                    if wybranekonto < len(self.UsersList):
                        print("Zalogowano się na konto użytkownika " + self.UsersList[wybranekonto].Name)
                        self.ZalogowanyUżytkownik = wybranekonto
                        break
                    else:
                        print("Nieprawidłowe informacje")
                        continue
            else:
                print("Nie ma żadnych kont użykownika w tym systemie")


    def WybórMenu(self):
        print("Wybierz zadanie jakie ma wykonać system")
        print("1. Dodawanie Nowych Kont\n2. Wypisz Użytkowników\n3. podzespoły serwera\n4. podzespoły zalogowanego konta\n5. Kod Administratora [Admin Only]\n6. Zmiana Danych [Admin, Redaktor Only]\n7. Wybór konta\n0. Zamknij System")
        while True:
            wybóropcji = int(input("Wybierz opcję: ") or 0)
            _timed = self.ZalogowaneKonto()
            if wybóropcji == 1:
                self.DodawanieNowychKont()
            elif wybóropcji == 2:
                self.WypiszIlośćUżytkowników()
            elif wybóropcji == 3:
                self.WyświetlPodzespoły()
            elif wybóropcji == 4:
                _timed.WyświetlPodzespoły()
            elif wybóropcji == 5:
                if _timed.Dostęp_Admin == True:
                    _timed.printkey()
                else:
                    print("Nie masz dostępy do tej komendy")
            elif wybóropcji == 6:
                if _timed.Dostęp_Admin == True or _timed.Dostęp_Redaktor == True:
                    _timed.ZmianaPól
                else:
                    print("nie masz dostępu do tej komendy")
            elif wybóropcji == 7:
                self.Wybórkonta()
            elif wybóropcji == 8:
                print(self.ZalogowaneKonto())
            elif wybóropcji == 4:
                break

    def ZalogowaneKonto(self):
        if self.ZalogowanyTypKonta == 1:
            return self.UsersList[self.ZalogowanyUżytkownik]
        if self.ZalogowanyTypKonta == 2:
            return self.RedaktorList[self.ZalogowanyRedaktor]
        if self.ZalogowanyTypKonta == 3:
            return self.AdminList[self.ZalogowanyAdmin]
            

    #### KLASA ADMIN ####    

class Admin(System):
    def __init__ (self,Procesor, KartaGraficzna, PamięcRam, Dysk, Name):
        super().__init__(Procesor, KartaGraficzna, PamięcRam, Dysk)
        self.Name = Name
        self.key = str(random.randrange(1000,9999))+"-"+str(random.randrange(1000,9999))+"-"+str(random.randrange(1000,9999))+"-"+str(random.randrange(1000,9999))
        self.ToSystem = False
        self.Dostęp_Admin = True
        self.Dostęp_Redaktor = False

    #### FUNKCJE W KLASIE "ADMIN" ####

    def printkey(self):
        print(self.key)

    def ZmienaPól(self):
        print("#### ZOSTAW POLE PUSTY BY GO NIE ZMIENIAĆ ####")
        input_name = input("Wpisz nową nazwę konta: ") or ""
        if input_name != "":
            self.Name = input_name
        input_key = input("Wpisz nowy kod administratora: ") or ""
        if input_key != "":
            self.key = input_key
        input_komp = input("Zmienić podzespoły komputera? [wcisnij dowolny klawisz]") or ""
        if input_komp != "":
            self.ZmienPodzespoły()

class Redaktor(System):
    def __init__ (self,Procesor, KartaGraficzna, PamięcRam, Dysk, Name):
        super().__init__(Procesor, KartaGraficzna, PamięcRam, Dysk)
        self.Name = Name
        self.ToSystem = False
        self.Dostęp_Admin = False
        self.Dostęp_Redaktor = True
    
    def ZmianaPól(self):
        print("zmiana pol")

class Użytkownik(System):
    def __init__ (self,Procesor, KartaGraficzna, PamięcRam, Dysk, Name):
        super().__init__(Procesor, KartaGraficzna, PamięcRam, Dysk)
        self.Name = Name
        self.ToSystem = False
        self.Dostęp_Admin = False
        self.Dostęp_Redaktor = False


GlassOS = System("","",0,0)
GlassOS.UruchamianieSystemu()
GlassOS.AdminList.append(Admin("","",0,0,""))
GlassOS.AdminList[len(GlassOS.AdminList) - 1].Name = input("Wpisz nazwę nowego konta: ")
GlassOS.WybórMenu()