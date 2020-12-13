f = open("C:\\Users\Overnex03\Documents\GitHub\ADIM\Piotrek\zadanie5\demofile.txt", "a") #a=dopisuje na koniec w=nadpisuje
f.write("Now the file has more content!")
f.close()

f = open("C:\\Users\Overnex03\Documents\GitHub\ADIM\Piotrek\zadanie5\demofile.txt", "r")
print(f.read())