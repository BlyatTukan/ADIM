import random

class KlasaPostaci:
    def __init__(self, Rasa, Imie, Nazwisko, Wiek, Wzrost, Moc, Broń, Pancerz): #dane postaci

        self.Rasa = Rasa #str
        self.Imie = Imie #str
        self.Nazwisko = Nazwisko #str
        self.Wiek = Wiek #int
        self.Wzrost = Wzrost #int
        self.Moc = Moc #str
        self.Broń = Broń #str
        self.Pancerz = Pancerz #str

        def Void(self):
            print("SELF")

        def GenerowaniePostaci(self):
            ### RASA
            self.Rasa = input("Podaj wartosc_float: ") or "Losowe"
            if self.Rasa == "Losowe":
                self.Rasa = random.choice(ListaRas)
                print("Wylosowane wartosc_float to " + self.Rasa)
            else:
                print("Wpisane wartosc_string to " + self.Rasa)
       
Postać = KlasaPostaci("","","",0,0,"","","")
Postać.Void()
