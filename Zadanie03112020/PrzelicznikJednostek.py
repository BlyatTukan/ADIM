def CelsjuszNaFahrenheit(C = 0.0):
    F = C * 1.8 + 32
    F = round(F, 1)
    print(str(F) + "C")

def FahrenheitNaCelsjusz(F = 0.0):
    C = (F-32)/1.8
    C = round(C, 1)
    print(str(C) + "F")

def KilogramyNaFunty(KG = 0.0):
    LB = KG*2.2046
    LB = round(LB, 2)
    print(str(LB) + "lb")

def FuntyNaKilogramy(LB = 0.0):
    KG = LB/2.2046
    KG = round(KG, 2)
    print(str(KG) + "KG")

def KMhNaMs(Kmh = 0):
    Ms = Kmh / 3.6
    Ms = round(Ms, 2)
    print(str(Ms) + "m/s")

def MpsNaKph(Ms = 0):
    Kmh = Ms * 3.6
    Kmh = round(Kmh, 2)
    print(str(Kmh) + "Km/h")
