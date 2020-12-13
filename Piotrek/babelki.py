import random

def Sortowanie(Lista):
    liczba = len(Lista)
  
    for Petla1 in range(liczba-1):
        for Petla2 in range(0, liczba-Petla1-1):
            if Lista[Petla2] > Lista[Petla2+1] : 
                Lista[Petla2], Lista[Petla2+1] = Lista[Petla2+1], Lista[Petla2]

Zbiór = [] 

x = random.randrange(0,20)
for i in range(0,x):
    Zbiór.append(0)

for i in range(len(Zbiór)): 
    Zbiór[i] = random.randrange(0,1000)

print("Przed Sortowaniem")
for i in range(len(Zbiór)): 
    print (Zbiór[i])

print("Po Sortowaniem")
Sortowanie(Zbiór) 
for i in range(len(Zbiór)): 
    print (Zbiór[i])