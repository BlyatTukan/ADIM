imie = input("Podaj sowje imię ")
nazwisko = input("Podaj swoje nazwisko ")

text = ("Oto twoje dane: " + "imie: " + imie + "  nazwisko: " + nazwisko + "\n")

Plik = open("C:\\Users\Overnex03\Documents\GitHub\ADIM\Piotrek\zadanie5\Test.txt", "a")
Plik.write(text)
Plik.close()

Plik = open("C:\\Users\Overnex03\Documents\GitHub\ADIM\Piotrek\zadanie5\Test.txt", "r")
print(Plik.read())
Plik.close()
