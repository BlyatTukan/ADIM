print("Witaj Użytkowniku")
print("Wpisz Magiczne Słowo")
MagicWord = str(input("Magiczne Słowo: ")) 
MagicWord = list(MagicWord) 
print("Czy chcesz bym zrobił kilka magicznych sztuczek z wpisanym słowem?") 
print("TAK - wpisz  T")
print("NIE - wpisz  N")
Magic = input("Odpowiedź: ")


print(MagicWord)


if "a" in MagicWord:
    print("Twoje Słowo zawiera litery A")
elif "A" in MagicWord:
    print("Twoje Słowo zawiera litery A")
else:
    print("Twoje Słowo nie zawiera litery A")

if "e" in MagicWord:
    print("Twoje Słowo zawiera litery e")
elif "E" in MagicWord:
    print("Twoje Słowo zawiera litery E")
else:
    print("Twoje Słowo nie zawiera litery E")

if "o" in MagicWord:
    print("Twoje Słowo zawiera litery o")
elif "O" in MagicWord:
    print("Twoje Słowo zawiera litery O")
else:
    print("Twoje Słowo nie zawiera litery O")


print("Pierwsza litera twojego magicznego słowa to " + MagicWord[0])
print("Ostatnią literą twojego magicznego słowa to " + MagicWord[-1])


MagicWord.insert(0, "Napisałeś: ")
print(''.join(MagicWord)) 