import math

pitagoras_c = lambda a, b : math.sqrt(int(a)**2 + int(b)**2)
pitagoras_b = lambda a, c : math.sqrt(int(c)**2 - int(a)**2)
pitagoras_a = lambda b, c : math.sqrt(int(c)**2 - int(a)**2)

ObjetoscKuli = lambda r : round(4.19*(int(r)**3),3)
PolePowieszchniKuli = lambda r : round(12.566 * int(r),3)
PrzekrojKuli = lambda r : round(4.19*int(r),3)

ObjętośćProstopadloscian = lambda a, b, c : int(a) * int(b) * int(c)
PoleProstopadloscian = lambda a, b, c : (2*int(a)*int(b)) + (2*int(c)*int(b)) + (2*int(a)*int(c))