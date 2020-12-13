try:
    plik = open("test.txt" , "r") 
    plik.read()
    plik.close()

except FileNotFoundError as d:
    print("plik nie istnieje")
    print(d)

except TypeError as d:
    print("Błędna linijka kodu")
    print(d)

except d:
    print("Nieznany błąd")
    print(d)

else:
    print("Wszystko jest ok")