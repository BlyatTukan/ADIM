import random

def Sortowanie(Lista):
    liczba = len(Lista)
  
    for Petla1 in range(liczba-1):
        for Petla2 in range(0, liczba-Petla1-1):
            czasowe = Lista[Petla2]
            if Lista[Petla2] > Lista[Petla2+1] : 
                Lista[Petla2] = Lista[Petla2+1]
                Lista[Petla2+1] = czasowe
    
    for i in range(len(Lista)): 
        print (Lista[i])


Zbiór = [] 
Losowość = True

print("Witaj w sortowniku liczb")
Ilość = int(input("Wpisz Ilość elementów do wygenerowania: [Standardowo jest 5]") or 5)
while True:
    LosowośćInput = input("Czy losowo wygenerować wszystkie liczby? ")
    if LosowośćInput == "Tak" or LosowośćInput == "tak" or LosowośćInput == "T" or LosowośćInput == "t" or LosowośćInput == "TAK":
        Losowość = True
        break
    elif LosowośćInput == "Nie" or LosowośćInput == "nie" or LosowośćInput == "N" or LosowośćInput == "n" or LosowośćInput == "NIE":
        Losowość = False
        break
    else:
        print("Nie prawidłowa Odpowiedź")
        continue

NajmniejszaIlość = int(input("Podaj Najmniejszą losową ilość: "))
NajwiększaIlość = int(input("Podaj Największa losową ilość: "))

if Losowość == False:
    print("[Klawisz Enter losuje daną liczbe]")
for i in range(0,Ilość):
    Zbiór.append(i)
    if Losowość == True:
        Zbiór[i] = random.randrange(NajmniejszaIlość,NajwiększaIlość)
    else:
        x = int(input("Podaj Wielkość Liczby: ") or -9238491749)
        if x == -9238491749:
            Zbiór[i] = random.randrange(NajmniejszaIlość,NajwiększaIlość)
        else:
            Zbiór[i] = x
        

for i in range(0,Ilość):
    print (Zbiór[i]) 

print("\nSortowanie:\n")

Sortowanie(Zbiór)